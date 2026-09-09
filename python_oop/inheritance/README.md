# Python - Inheritance & Polymorphism

## Description

Ce projet introduit les concepts d'**héritage** et de **polymorphisme** en Python.

L'objectif est de construire progressivement une hiérarchie de classes représentant des formes géométriques :

```text
BaseGeometry
      |
      v
  Rectangle
      |
      v
    Square
```

Le projet permet notamment de comprendre comment une classe peut réutiliser les attributs et méthodes d'une autre classe, comment redéfinir une méthode héritée et comment vérifier les relations entre objets et classes.

## Learning Objectives

À la fin de ce projet, je dois être capable de :

* expliquer comment l'héritage permet de réutiliser un comportement ;
* identifier une classe parente et une classe enfant ;
* créer une sous-classe ;
* étendre le comportement d'une classe ;
* redéfinir une méthode héritée ;
* comprendre le polymorphisme ;
* utiliser `isinstance()` ;
* utiliser `issubclass()` ;
* construire une hiérarchie simple de classes.

## Class Hierarchy

```text
BaseGeometry
      |
      v
  Rectangle
      |
      v
    Square
```

* `Rectangle` hérite de `BaseGeometry`.
* `Square` hérite de `Rectangle`.
* `Square` est donc également lié à `BaseGeometry` par héritage.

## Requirements

* Ubuntu 20.04
* Python 3.8
* PEP8
* Tous les fichiers Python doivent être exécutables.
* Tous les fichiers Python doivent commencer par :

```python
#!/usr/bin/env python3
```

* Tous les fichiers doivent se terminer par une nouvelle ligne.
* Tous les modules, classes et fonctions doivent posséder une docstring.
* Seule la bibliothèque standard Python peut être utilisée, sauf indication contraire.
* Les mots `import` et `from` ne doivent pas apparaître dans les commentaires.
* Pour importer une classe de base, utiliser la méthode `__import__`.

## Resources

* Python Documentation — Classes
* Python Documentation — `isinstance()`
* Python Documentation — `issubclass()`
* Python Tutorial — Class Inheritance
* Real Python — Inheritance and Composition
* Programiz — Method Overriding in Python
* W3Schools — Python Inheritance

## Project Structure

Les fichiers et exercices seront ajoutés progressivement au fur et à mesure des tâches du projet.
