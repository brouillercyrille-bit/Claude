# Challenge IA — Dstny Digital Assistant

Suivi hebdomadaire du challenge commercial : nombre d'intérêts partenaires pour Dstny Digital Assistant (IA) et pipeline de projets clients finaux (fin 2026 et 2027).

## Historique semaine par semaine

Chaque export HubSpot est archivé dans un dossier daté par semaine ISO, jamais écrasé :

```
challenge-ia/
  historique.csv                 # une ligne par semaine : KPI clés (intérêts, pipeline 2026, pipeline 2027…)
  semaines/
    2026-S40/                    # semaine ISO (année-Snuméro)
      export-hubspot-<date>.csv  # export brut tel que reçu
      donnees-normalisees.csv    # export nettoyé, colonnes harmonisées
      graphiques/                # PNG des graphiques de la semaine
      analyse.md                 # analyse et messages clés de la semaine
      slides/                    # copie des slides (deck en ligne, lien dans analyse.md)
```

Pour retrouver une semaine passée : ouvrir `semaines/<année>-S<numéro>/`. Les évolutions d'une semaine sur l'autre sont calculées à partir de `historique.csv`.

## Évolutions semaine par semaine

Chaque semaine est comparée à la précédente avec `scripts/suivi.py` (procédure complète dans le `CLAUDE.md` à la racine) :

```
python3 challenge-ia/scripts/suivi.py ingest 2026-S41 <export_interet> <export_opportunites>
python3 challenge-ia/scripts/suivi.py compare 2026-S40 2026-S41
```

`evolution.md` donne les écarts de chaque indicateur, les partenaires qui changent de statut d'intérêt, les nouveaux projets clients finaux, ceux qui sortent du rapport, les changements de phase et les dates de closing qui glissent. Les exports arrivent chaque lundi matin. **La référence est l'import du lundi 5 octobre 2026 (2026-S41)** : les évolutions sont calculées à partir de la S42. La S40 (export du jeudi 01/10/2026) est un point de départ provisoire, conservé pour mémoire.
