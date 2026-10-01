# MRR Partenaires

Tableau de bord RevOps pour suivre le MRR généré par les nouveaux partenaires recrutés par chaque commercial (objectif par défaut : 500 € / commercial / mois).

- **Tableau de bord** : KPI, performance par commercial vs objectif à date, évolution mensuelle, détail mois par mois, classement, top partenaires. Filtres mois / trimestre / année / tout et par commercial. Export CSV.
- **Saisie MRR mensuel** : ajout d'un partenaire (nom, commercial, mois de recrutement, OIP, types de produit DFP à cocher dans une liste), puis grille annuelle partenaires × mois pour saisir le nouveau MRR généré chaque mois (un partenaire recruté en février peut produire du MRR en avril, mai, juin…). Le mois de recrutement, l'OIP et le type de produit DFP se corrigent directement dans la grille.
- **Partenaires** : liste, recherche, modification et suppression.
- **Équipe & objectifs** : liste des types de produit DFP (modifiable), commerciaux (ajout, renommage, activation) et objectif mensuel par commercial, réglable mois par mois (par défaut 500 € ; 2026 : janvier 0 €, février 150 €, mars 300 €, août 50 €).

Publiée comme artifact claude.ai, la page stocke les données dans une base partagée. Ouverte en local (`index.html`), elle les garde dans le navigateur (localStorage) et propose un jeu d'exemple.
