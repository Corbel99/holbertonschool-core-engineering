# Python - Functions & Modularity

## Introduction

À mesure que les programmes grandissent, répéter la même logique devient inefficace et augmente les risques d'erreurs.

Les **fonctions** permettent d'encapsuler un comportement dans des blocs de code réutilisables.

Les **modules** permettent d'organiser ces fonctions dans différents fichiers et de les réutiliser correctement.

Ce projet introduit progressivement :

* la définition des fonctions et les valeurs de retour ;
* le déroulement de l'exécution à l'intérieur et à l'extérieur des fonctions ;
* la distinction entre `print` et `return` ;
* la manière dont Python exécute un fichier ;
* l'effet de l'importation d'un fichier sur son exécution ;
* la réutilisation de fonctions et de variables provenant d'autres fichiers.

L'ordre des exercices est intentionnel. Le projet progresse de la définition de fonctions jusqu'à l'organisation sûre du code dans plusieurs fichiers.

---

## Objectifs d'apprentissage

À la fin de ce projet, je dois être capable de :

* définir des fonctions avec des paramètres et des valeurs de retour ;
* distinguer clairement `print` et `return` ;
* implémenter une logique dans des fonctions avec des conditions et des boucles ;
* comprendre comment Python exécute le code situé au niveau principal d'un fichier ;
* expliquer ce que fait `if __name__ == "__main__"` et pourquoi il est nécessaire ;
* importer des fonctions depuis d'autres fichiers ;
* importer des variables depuis d'autres fichiers ;
* écrire des scripts qui se comportent correctement lorsqu'ils sont exécutés directement et lorsqu'ils sont importés.

---

## Ressources

* Python Tutorial — Defining Functions
  https://docs.python.org/3/tutorial/controlflow.html#defining-functions

* Python Tutorial — Modules
  https://docs.python.org/3/tutorial/modules.html

* Python Reference — `__name__`
  https://docs.python.org/3/library/__main__.html

* PEP8 Style Guide
  https://peps.python.org/pep-0008/

---

## Contraintes générales

Les corrections seront exécutées sur :

* **Ubuntu 20.04 LTS**
* **Python 3.8.x**

### Fichiers Python

La première ligne de chaque fichier Python doit être exactement :

```python
#!/usr/bin/env python3
```

Tous les fichiers doivent :

* être exécutables ;
* se terminer par une nouvelle ligne ;
* respecter le style **PEP8** ;
* être compatibles avec **pycodestyle 2.7.x**.

### Bibliothèques

Aucune bibliothèque externe n'est autorisée.

### Arguments

L'utilisation de `sys.argv` est interdite dans ce projet.

### Exercices

Chaque tâche doit respecter précisément ses propres contraintes.

---

# Tasks

## 0. islower

### Objectif

Écrire une fonction :

```python
def islower(c):
```

La fonction doit retourner :

* `True` si `c` est une lettre minuscule ;
* `False` dans tous les autres cas.

### Contraintes

* Ne pas utiliser les méthodes intégrées des chaînes de caractères telles que `.islower()`.
* Utiliser la logique ASCII avec `ord()`.
* La fonction doit retourner une valeur booléenne.

### Exemples

```python
>>> islower('a')
True
>>> islower('A')
False
>>> islower('3')
False
```

### Dépôt

**Repository :**

`holbertonschool-core-engineering`

**Directory :**

`python_fundamentals/functions_modules`

**File :**

`islower.py`

---

## Progression du projet

Le projet suit progressivement cette logique :

```text
Fonctions
    ↓
Paramètres
    ↓
Valeurs de retour
    ↓
print vs return
    ↓
Conditions et boucles
    ↓
Exécution d'un fichier Python
    ↓
__name__ == "__main__"
    ↓
Importation de fonctions
    ↓
Importation de variables
    ↓
Modularité
```

L'objectif général est de comprendre **comment écrire des fonctions réutilisables et comment organiser correctement du code Python dans plusieurs fichiers**.
