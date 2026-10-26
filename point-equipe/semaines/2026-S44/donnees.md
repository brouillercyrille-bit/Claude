# Point équipe — S44 (lundi 26/10/2026)

Exports S42 et S43 non reçus : comparaison avec la S41 (05/10).

## Partenaires recrutés
- Source : `export-hubspot-partenaires-recrutes.xlsx` (export CRM « Partenaires recrutés », 26/10/2026, nouveau format : une ligne par transaction avec l'entreprise principale, dates d'entrée dans les phases).
- Recrutés à date (phase « Partenaire recruté ») : **50**. Ce sont les 50 mêmes transactions qu'au 05/10 : **0 nouveau recrutement**. Le 05/10 on comptait 51 entreprises car PC PRO TECH / EVO TELECOM était rattachée à 2 entreprises ; le nouvel export ne garde que l'entreprise principale.
- T3 2026 (date de fermeture du 01/07 au 30/09) : **16**, inchangé. Avec la date d'entrée en « Partenaire recruté », on trouve aussi 16.
- Prêts pour formation (étape avant le recrutement) : **18**, nouveaux dans l'export.
- Objectif : non fourni.

## Points de qualité
- 8 transactions « Prêt pour formation » ont une date de fermeture déjà passée (du 17/06 au 09/10/2026).
- 2 transactions « Prêt pour formation » appartiennent à des utilisateurs désactivés (GPCONSULT - ALTER ILLICO, ACESI GROUP).
- Dates d'entrée en « Partenaire recruté » saisies en masse : 11 le 25/09 entre 14h37 et 14h42, 4 le 29/01 à 10h27.
- Écart entre trimestre de recrutement (date d'entrée dans la phase) et trimestre de fermeture : T1 22 vs 12, T2 11 vs 21.

## Projets ops en cours
Inchangés (pas de mise à jour reçue) : boîte à idées des commerciaux, clean des contacts (nom et prénom), renseigner l'intégration avec l'outil IA.

## Toutes les transactions (pipeline Prospection partenaire)
- Source : `export-hubspot-toutes-transactions.xlsx` (26/10/2026), 237 transactions : Fermé perdu 52, Partenaire recruté 50, Rendez-vous planifié 48, Pitch réalisé 30, Intérêt confirmé (deal) 25, Prêt pour formation 18, Formulaire renseigné 7, Approbation du partenaire 7.
- Demande : nombre de transactions sans mouvement depuis plus de 30 jours et sans contact depuis plus de 30 jours. **Non calculable** : l'export ne contient ni date de dernière modification, ni date de dernière activité / dernier contact.
- Ouvertes : 135 (hors Partenaire recruté et Fermé perdu). Indicateur de remplacement : 62 ont une date de fermeture passée, dont 45 depuis plus de 30 jours (Mathys Bechu 15, Alain Babaci 12, Vincent Del Campo 6, Tristan Eckel 6 (désactivé), Jonathan Zbinden 3, Eric Maury 2 (désactivé), Matthis Le Castrec 1).
- 8 transactions ouvertes appartiennent à des utilisateurs désactivés.
- Slides « Prospection partenaires » et « Deals inactifs » ajoutées au deck challenge S44.

## Deals inactifs (export « État du pipe », 26/10/2026)
- Source : `export-hubspot-etat-du-pipe.xlsx` (237 transactions, avec « Dernier contact » et dates d'entrée/sortie de chaque phase). Détail par deal : `deals-ouverts-inactivite.csv`.
- Périmètre : 135 transactions ouvertes (hors Partenaire recruté et Fermé perdu). Phases : Rendez-vous planifié 48, Pitch réalisé 30, Intérêt confirmé (deal) 25, Prêt pour formation 20, Formulaire renseigné 7, Approbation du partenaire 5 (2 deals passés d'Approbation à Prêt pour formation depuis l'export du matin : PRIMAXION, CEDELIA).
- **Sans mouvement > 30 jours** (entrée dans la phase actuelle avant le 26/09) : **120**.
- **Sans contact > 30 jours** (dernier contact avant le 26/09 ou jamais) : **98**, dont 22 jamais contactés.
- **Les deux** : **93**.
- Par commercial (les deux / ouverts) : Vincent Del Campo 20/22, Stéphanie Martinage 13/18, Sylvain Gotrand 12/13, Mathys Bechu 11/17, Christophe Dorey 10/13, Alain Babaci 8/15, Tristan Eckel (désactivé) 6/6, Corinne Baroukh 4/9, Jonathan Zbinden 3/6, Matthis Le Castrec 2/3, Eric Maury (désactivé) 2/2, Cyrille Brouiller 1/1, Jennifer Pereira 1/10.
- Médianes : 216 jours dans la phase actuelle, 144 jours depuis le dernier contact. 81 deals dans leur phase depuis plus de 6 mois.
