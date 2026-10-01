# Contexte

RevOps Dstny. Ce dépôt contient les outils de suivi commercial :
- `mrr-partenaires/` : tableau de bord MRR des nouveaux partenaires.
- `challenge-ia/` : suivi hebdomadaire du challenge Dstny Digital Assistant (IA), voir son README.

# Challenge IA : procédure à chaque nouvel export HubSpot

L'utilisateur envoie chaque **lundi matin** deux exports HubSpot : « Partenaires - Intérêt IA » et « Partenaires - Opportunités IA ».

**Référence : l'import du lundi 5 octobre 2026 (2026-S41).** Il n'a pas d'évolution à montrer ; les comparaisons commencent avec la S42 (lundi 12/10 vs lundi 05/10). La S40 (export du jeudi 01/10/2026) est un point de départ provisoire, archivé mais jamais utilisé comme base de comparaison.

1. Archiver et normaliser : `python3 challenge-ia/scripts/suivi.py ingest <AAAA-Snn> <export_interet> <export_opportunites>` (semaine ISO du lundi de l'export, ex. lundi 05/10/2026 = 2026-S41). Si l'utilisateur renvoie un export corrigé pour une semaine déjà archivée, relancer `ingest` sur la même semaine : la ligne d'historique est remplacée.
2. **Toujours comparer à la semaine précédente** : `python3 challenge-ia/scripts/suivi.py compare <lundi précédent> <semaine>` (à partir de la S42 ; la S41 est la référence) → `semaines/<semaine>/evolution.md`.
3. Écrire `semaines/<semaine>/analyse.md` et les graphiques, puis le deck de la réunion commerciale (artifact Slides). Le deck doit contenir les évolutions vs S-1 : écarts sur chaque KPI dans la synthèse, une slide « Évolution vs semaine précédente » (statuts partenaires qui progressent ou reculent, nouveaux projets, projets sortis, changements de phase, dates de closing qui glissent), et la courbe des semaines depuis `historique.csv` dès qu'il y a 3 semaines ou plus.
4. Commit et push de `challenge-ia/` sur la branche de travail : l'historique doit être conservé semaine par semaine.

Règles de présentation :
- Bien distinguer **intérêt partenaires** (teal, propriété « Intérêt Dstny Digital Assistant » sur le partenaire) et **projets clients finaux** (prune, transactions IA du Pipeline VI). Orange réservé aux alertes.
- Il n'existe pas de champ « partenaires qualifiés » : ne pas l'utiliser.
- Toujours inclure une slide de vue d'ensemble sans nom de commercial.
- Français, chiffres sourcés des exports, jamais de valeur inventée.
