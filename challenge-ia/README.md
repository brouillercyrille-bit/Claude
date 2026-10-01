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
