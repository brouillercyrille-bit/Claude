# Challenge IA — Semaine 40 (exports du 01/10/2026, version corrigée)

Deck de la réunion : https://claude.ai/artifact/1F7i7xrzY2e1eJvb45tgaL (copie des slides dans `slides/`).

## Sources
- `export-hubspot-interet-ia-2026-10-01.csv` (+ `-synthese.csv`) : rapport « Partenaires - Intérêt IA », 120 partenaires avec un statut d'intérêt renseigné (statut + ID entreprise). Remplace un premier export erroné (21 partenaires).
- `export-hubspot-opportunites-ia-2026-10-01.xlsx` : rapport « Partenaires - Opportunités IA », 11 transactions (inchangé par rapport au premier export).

Deux indicateurs distincts : l'**intérêt partenaires** (propriété « Intérêt Dstny Digital Assistant » sur la fiche du partenaire) et les **projets clients finaux** (transactions IA du Pipeline VI).

## Chiffres clés
| Indicateur | S40 |
|---|---|
| **Intérêt partenaires** | |
| Partenaires avec un statut renseigné | 120 |
| Intérêt (à confirmer) | 75 |
| Intérêt confirmé | 22 |
| Pas intéressé | 23 |
| Partenaires intéressés (intérêt + confirmé) | 97 |
| **Projets clients finaux** | |
| Opportunités IA | 11, chez 10 partenaires |
| dont Projet détecté / Deal en cours | 9 / 2 |
| Closing oct. / nov. / déc. 2026 / 2027 | 6 / 3 / 2 / 0 |

Opportunités par commercial : Corinne Baroukh 5 (1 en cours), Jennifer Pereira 3, Alain Babaci 2 (1 en cours), Vincent Del Campo 1.

## Analyse
1. **Fort intérêt, confirmation à travailler** : 97 partenaires intéressés contre 23 pas intéressés ; 22 intérêts confirmés, 75 restent à confirmer.
2. **Peu de conversion en projets** : seuls 3 des 97 partenaires intéressés ont un projet client final, tous au statut confirmé (Corinne 2, Alain 1). 19 confirmés n'ont pas encore de projet : priorité pour alimenter le pipeline 2027.
3. **Propriété Intérêt pas à jour** : 7 partenaires ont un projet sans intérêt renseigné (Corinne 3, Jennifer 3, Vincent 1). On compterait plutôt 104 partenaires intéressés.
4. **Dates de closing optimistes** : 6 closings en octobre, dont 4 encore au stade « Projet détecté » (un au 16/10).
5. **Doublon probable** : Alain Babaci a 2 deals sur le même partenaire (ID 10061742314, intérêt confirmé), créés à la suite, closing au 30/10.
6. **Pipeline 2027 vide** : aucune opportunité datée 2027.

## Limites de l'export
- Pas de propriétaire dans le rapport Intérêt : pas de classement des intérêts par commercial.
- Pas de montant : pas de valeur de pipeline.
- Pas de nom d'entreprise ni de date de création.

## Colonnes demandées pour la S41
- Rapport Intérêt : propriétaire de l'entreprise, nom de l'entreprise, date de mise à jour de l'intérêt.
- Rapport Opportunités : montant, nom du deal / client final, nom du partenaire, date de création.
