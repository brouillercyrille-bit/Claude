# Challenge IA — Semaine 40 (export du 01/10/2026)

Deck de la réunion : https://claude.ai/artifact/1F7i7xrzY2e1eJvb45tgaL (copie des slides dans `slides/`).

## Sources
- `export-hubspot-interet-ia-2026-10-01.xlsx` : rapport « Partenaires - Intérêt IA », 21 partenaires avec un statut d'intérêt renseigné (statut + ID entreprise). Il n'existe pas de champ « partenaire qualifié ».
- `export-hubspot-opportunites-ia-2026-10-01.xlsx` : rapport « Partenaires - Opportunités IA », 11 transactions (phase, propriétaire, produit, date de fermeture, ID entreprise).

## Chiffres clés

Deux indicateurs distincts : l'**intérêt partenaires** (propriété « Intérêt Dstny Digital Assistant » sur la fiche du partenaire) et les **projets clients finaux** (transactions IA du Pipeline VI).
| Indicateur | S40 |
|---|---|
| **Intérêt partenaires** | |
| Partenaires intéressés | 17 |
| Intérêt (à confirmer) | 13 |
| Intérêt confirmé | 4 |
| Pas intéressé | 4 |
| **Projets clients finaux** | |
| Opportunités IA (projets clients finaux) | 11, chez 10 partenaires |
| dont Projet détecté / Deal en cours | 9 / 2 |
| Closing oct. / nov. / déc. 2026 / 2027 | 6 / 3 / 2 / 0 |

Opportunités par commercial : Corinne Baroukh 5 (1 en cours), Jennifer Pereira 3, Alain Babaci 2 (1 en cours), Vincent Del Campo 1.

## Analyse
1. **Fort intérêt, faible confirmation** : 17 partenaires intéressés contre 4 pas intéressés, mais seulement 4 intérêts confirmés.
2. **Peu de conversion en projets** : seuls 2 des 17 partenaires intéressés ont une opportunité IA. Les 13 au statut « Intérêt » n'en ont aucune : c'est le vivier pour 2027.
3. **Propriété Intérêt pas à jour** : 8 partenaires ont une opportunité IA sans intérêt renseigné (Corinne 3, Jennifer 3, Alain 1, Vincent 1). Le nombre réel de partenaires intéressés est plutôt de 25.
4. **Dates de closing optimistes** : 6 closings en octobre, dont 4 encore au stade « Projet détecté » (un au 16/10).
5. **Doublon probable** : Alain Babaci a 2 deals sur le même partenaire (ID 10061742314), créés à la suite, closing au 30/10.
6. **Pipeline 2027 vide** : aucune opportunité datée 2027.

## Limites de l'export
- Pas de propriétaire dans le rapport Intérêt : pas de classement des intérêts par commercial.
- Pas de montant : pas de valeur de pipeline.
- Pas de nom d'entreprise ni de date de création.

## Colonnes demandées pour la S41
- Rapport Intérêt : propriétaire de l'entreprise, nom de l'entreprise, date de mise à jour de l'intérêt.
- Rapport Opportunités : montant, nom du deal / client final, nom du partenaire, date de création.
