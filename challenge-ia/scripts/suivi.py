"""Suivi hebdomadaire du challenge IA.

  python3 suivi.py ingest 2026-S41 <export_interet> <export_opportunites>
      Archive les exports bruts dans semaines/<semaine>/, écrit les CSV normalisés
      et ajoute (ou remplace) la ligne de la semaine dans historique.csv.
  python3 suivi.py compare 2026-S40 2026-S41
      Écrit semaines/<semaine>/evolution.md : écarts de KPI, changements de statut
      des partenaires, nouveaux projets, projets sortis, changements de phase et de date.
"""
import shutil, sys, warnings
from pathlib import Path
import pandas as pd

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parent.parent
WEEKS = ROOT / "semaines"
HIST = ROOT / "historique.csv"
INTERESTED = ["Intérêt", "Intérêt confirmé"]
RANK = {"Pas intéressé": 0, "Intérêt": 1, "Intérêt confirmé": 2}

COLS = {
    "Intérêt Dstny Digital Assistant": "interet", "Entreprise ID": "entreprise_id",
    "Phase de la transaction": "phase", "Propriétaire de la transaction": "commercial",
    "Propriétaire de l'entreprise": "commercial", "Type de Produit (DFP)": "produit",
    "Date de fermeture": "date_fermeture", "Transaction ID": "transaction_id",
    "Montant": "montant", "Nom de la transaction": "nom_transaction",
    "Nom de l'entreprise": "nom_entreprise", "Date de création": "date_creation",
}


def read_export(path):
    """Detail sheet of a HubSpot xlsx (the non-summary one), a csv, or a zip holding one."""
    path = Path(path)
    if path.suffix == ".zip":
        import zipfile
        with zipfile.ZipFile(path) as z:
            name = next(n for n in z.namelist() if n.endswith(".csv") and "summary" not in n.lower())
            with z.open(name) as f:
                return pd.read_csv(f)
    if path.suffix == ".csv":
        return pd.read_csv(path)
    x = pd.ExcelFile(path)
    return x.parse(next(s for s in x.sheet_names if "summary" not in s.lower()))


def normalize(df):
    df = df.rename(columns={c: COLS.get(c.strip(), c.strip()) for c in df.columns})
    if "phase" in df:
        df["phase"] = df.phase.str.replace(r"\s*\(Pipeline VI\)", "", regex=True).str.strip()
    if "commercial" in df:
        df["commercial"] = df.commercial.fillna("Non attribué").str.strip().str.title()
    if "date_fermeture" in df:
        df["date_fermeture"] = pd.to_datetime(df.date_fermeture).dt.date
    return df


def load(week):
    d = WEEKS / week
    o = pd.read_csv(d / "opportunites-normalisees.csv", parse_dates=["date_fermeture"])
    o["commercial"] = o.commercial.fillna("Non attribué").str.strip().str.title()
    return pd.read_csv(d / "interet-normalise.csv"), o


def kpis(week, i, o):
    year = pd.to_datetime(o.date_fermeture).dt.year
    status = o.entreprise_id.map(dict(zip(i.entreprise_id, i.interet)))
    k = {
        "semaine": week,
        "interet_a_confirmer": int((i.interet == "Intérêt").sum()),
        "interet_confirme": int((i.interet == "Intérêt confirmé").sum()),
        "pas_interesse": int((i.interet == "Pas intéressé").sum()),
        "partenaires_interesses": int(i.interet.isin(INTERESTED).sum()),
        "partenaires_interesses_avec_projet": int(i[i.interet.isin(INTERESTED)].entreprise_id.isin(o.entreprise_id).sum()),
        "partenaires_avec_projet_sans_interet": int(o[status.isna()].entreprise_id.nunique()),
        "opportunites_ia": len(o),
        "opps_projet_detecte": int((o.phase == "Projet détecté").sum()),
        "opps_deal_en_cours": int((o.phase == "Deal en cours").sum()),
        "opps_closing_2026": int((year == 2026).sum()),
        "opps_closing_2027": int((year == 2027).sum()),
    }
    if "montant" in o:
        k["montant_pipeline"] = float(o.montant.fillna(0).sum())
    for name, n in o.commercial.value_counts().items():
        k["opps_" + name.lower().replace(" ", "_")] = int(n)
    return k


def ingest(week, interet_path, opp_path):
    d = WEEKS / week
    (d / "graphiques").mkdir(parents=True, exist_ok=True)
    for src, kind in [(interet_path, "interet"), (opp_path, "opportunites")]:
        shutil.copy(src, d / f"export-hubspot-{kind}-ia{Path(src).suffix}")
    i, o = normalize(read_export(interet_path)), normalize(read_export(opp_path))
    o["statut_interet_partenaire"] = o.entreprise_id.map(dict(zip(i.entreprise_id, i.interet))).fillna("Non renseigné")
    i["a_une_opportunite"] = i.entreprise_id.isin(o.entreprise_id).map({True: "Oui", False: "Non"})
    i.to_csv(d / "interet-normalise.csv", index=False)
    o.sort_values("transaction_id").to_csv(d / "opportunites-normalisees.csv", index=False)
    hist = pd.read_csv(HIST) if HIST.exists() else pd.DataFrame()
    row = kpis(week, *load(week))
    hist = pd.concat([hist[hist.semaine != week] if len(hist) else hist, pd.DataFrame([row])], ignore_index=True)
    hist.sort_values("semaine").to_csv(HIST, index=False)
    print(pd.Series(row).to_string())


def compare(prev, cur):
    i0, o0 = load(prev)
    i1, o1 = load(cur)
    k0, k1 = kpis(prev, i0, o0), kpis(cur, i1, o1)
    out = [f"# Évolution {cur} vs {prev}", "", "## Indicateurs", "", f"| Indicateur | {prev} | {cur} | Écart |", "|---|---|---|---|"]
    for key in [k for k in k1 if k != "semaine"] + [k for k in k0 if k not in k1 and k != "semaine"]:
        a, b = k0.get(key, 0), k1.get(key, 0)
        out.append(f"| {key} | {a:g} | {b:g} | {b - a:+g} |")

    s0, s1 = dict(zip(i0.entreprise_id, i0.interet)), dict(zip(i1.entreprise_id, i1.interet))
    moves = [(e, s0.get(e, "Non renseigné"), s1.get(e, "Non renseigné")) for e in set(s0) | set(s1) if s0.get(e) != s1.get(e)]
    up = [m for m in moves if RANK.get(m[2], -1) > RANK.get(m[1], -1)]
    down = [m for m in moves if m not in up]
    out += ["", "## Intérêt partenaires : changements de statut", "",
            f"{len(moves)} partenaires ont changé de statut : {len(up)} progressions, {len(down)} reculs ou retraits.", ""]
    for title, rows in [("Progressions", up), ("Reculs ou retraits", down)]:
        if rows:
            out += [f"**{title}**", "", "| Entreprise ID | Avant | Maintenant |", "|---|---|---|"]
            out += [f"| {e} | {a} | {b} |" for e, a, b in sorted(rows, key=lambda m: (m[2], m[0]))] + [""]
    trans = pd.crosstab(pd.Series([m[1] for m in moves], name="avant"), pd.Series([m[2] for m in moves], name="maintenant")) if moves else None
    if trans is not None:
        out += ["**Matrice des transitions**", "", "```", trans.to_string(), "```", ""]

    a, b = o0.set_index("transaction_id"), o1.set_index("transaction_id")
    new, gone, both = b.index.difference(a.index), a.index.difference(b.index), a.index.intersection(b.index)
    out += ["## Projets clients finaux : mouvements", "",
            f"- Nouveaux projets : {len(new)}", f"- Projets sortis du rapport (gagnés, perdus ou hors IA) : {len(gone)}"]
    stage = [t for t in both if a.at[t, "phase"] != b.at[t, "phase"]]
    dates = [t for t in both if a.at[t, "date_fermeture"] != b.at[t, "date_fermeture"]]
    owner = [t for t in both if a.at[t, "commercial"] != b.at[t, "commercial"]]
    out += [f"- Changements de phase : {len(stage)}", f"- Dates de closing modifiées : {len(dates)}", f"- Changements de commercial : {len(owner)}", ""]

    def table(title, ids, df, cols):
        if len(ids):
            nonlocal out
            out += [f"**{title}**", "", "| Transaction ID | " + " | ".join(cols) + " |", "|---" * (len(cols) + 1) + "|"]
            out += [f"| {t} | " + " | ".join(str(df.at[t, c])[:10] if c == "date_fermeture" else str(df.at[t, c]) for c in cols) + " |" for t in ids] + [""]

    table("Nouveaux projets", new, b, ["commercial", "phase", "date_fermeture", "entreprise_id"])
    table("Projets sortis", gone, a, ["commercial", "phase", "date_fermeture", "entreprise_id"])
    if stage:
        out += ["**Changements de phase**", "", "| Transaction ID | Commercial | Avant | Maintenant |", "|---|---|---|---|"]
        out += [f"| {t} | {b.at[t, 'commercial']} | {a.at[t, 'phase']} | {b.at[t, 'phase']} |" for t in stage] + [""]
    if dates:
        out += ["**Dates de closing modifiées**", "", "| Transaction ID | Commercial | Avant | Maintenant | Glissement (jours) |", "|---|---|---|---|---|"]
        out += [f"| {t} | {b.at[t, 'commercial']} | {a.at[t, 'date_fermeture']:%d/%m/%Y} | {b.at[t, 'date_fermeture']:%d/%m/%Y} | {(b.at[t, 'date_fermeture'] - a.at[t, 'date_fermeture']).days:+d} |" for t in dates] + [""]

    per = pd.DataFrame({prev: o0.commercial.value_counts(), cur: o1.commercial.value_counts()}).fillna(0).astype(int)
    per["écart"] = per[cur] - per[prev]
    out += ["## Projets clients finaux par commercial", "", "| Commercial | " + f"{prev} | {cur} | Écart |", "|---|---|---|---|"]
    out += [f"| {n} | {r[prev]} | {r[cur]} | {r['écart']:+d} |" for n, r in per.sort_values(cur, ascending=False).iterrows()]
    path = WEEKS / cur / "evolution.md"
    path.write_text("\n".join(out) + "\n")
    print(path.read_text())


if __name__ == "__main__":
    cmd, *args = sys.argv[1:]
    {"ingest": ingest, "compare": compare}[cmd](*args)
