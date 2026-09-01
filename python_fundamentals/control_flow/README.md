# Python - Control Flow

## Description

Ce projet permet de découvrir le contrôle du flux en Python.

Le contrôle du flux permet à un programme de :

- exécuter différentes instructions selon une condition ;
- répéter des instructions avec des boucles ;
- combiner plusieurs conditions logiques.

Le projet porte principalement sur :

- `if`
- `elif`
- `else`
- les opérateurs de comparaison ;
- la logique booléenne ;
- les boucles `while` ;
- les boucles `for` avec `range()`.

## Objectifs

À la fin du projet, je dois être capable de :

- écrire des conditions avec `if`, `elif` et `else` ;
- utiliser correctement les opérateurs de comparaison et logiques ;
- utiliser `while` et `for` pour répéter des instructions ;
- comprendre les limites et les différentes itérations d'une boucle ;
- produire une sortie formatée ;
- combiner des conditions et des boucles pour obtenir un résultat déterministe.

## Contraintes

- Les corrections sont effectuées sur Ubuntu 20.04 LTS.
- La version de Python utilisée est Python 3.8.x.
- Chaque fichier Python doit commencer exactement par :
  `#!/usr/bin/env python3`
- Chaque fichier doit être exécutable.
- Chaque fichier doit se terminer par une nouvelle ligne.
- Le code doit respecter PEP8 avec `pycodestyle 2.7.x`.
- Aucune bibliothèque externe n'est autorisée.
- Aucune fonction ne doit être créée dans ce projet.
- Aucun import ne doit être utilisé.
- La sortie doit respecter exactement le format attendu.

## Ressources

- Python Tutorial — Control Flow Tools
  https://docs.python.org/3/tutorial/controlflow.html

- Python Tutorial — More on Conditions
  https://docs.python.org/3/reference/expressions.html#comparisons

## Tâches

### 0. Positive anything is better than negative nothing

Créer un script qui attribue un entier aléatoire à une variable appelée `number`.

Le programme utilise ensuite des conditions pour afficher :

- `<number> is positive` si le nombre est supérieur à `0` ;
- `<number> is zero` si le nombre est égal à `0` ;
- `<number> is negative` si le nombre est inférieur à `0`.

La structure utilisée est :

```text
if
 ↓
elif
 ↓
else