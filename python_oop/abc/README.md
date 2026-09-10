# Python - Abstract Classes & Interfaces

## Introduction and Context

In object-oriented programming, some classes are used to define a **common contract** for other classes.

Sometimes a class should define **what behavior must exist**, but should not provide the full implementation itself. In Python, this can be modeled using **abstract classes**.

An abstract class allows you to define methods that subclasses are expected to implement. This helps create consistent designs where different objects share the same interface while keeping their own specific behavior.

A related concept is the idea of an **interface**. Python does not have a dedicated `interface` keyword, but similar results can be achieved using abstract methods or by relying on **duck typing**.

In this project, you will work with:

* abstract base classes
* abstract methods
* interface-like design
* duck typing
* subclassing built-in classes
* multiple inheritance
* mixins

These tools are useful when building flexible and reusable software designs.

---

## Learning Objectives

By completing this project, you should be able to:

* explain the purpose of an **abstract class**
* use `ABC` and `@abstractmethod`
* implement subclasses that satisfy an abstract contract
* understand how Python can model **interfaces**
* explain and apply **duck typing**
* extend built-in classes while preserving their behavior
* understand the role of **multiple inheritance**
* use **mixins** to add reusable behavior to a class

---

## Concept Guide

### Abstract Classes and Concrete Classes

An **abstract class** defines behavior that subclasses must implement.

Example:

```text
          Animal (Abstract Class)
                 │
        ┌────────┴────────┐
        │                 │
       Dog               Cat
   (Concrete Class)  (Concrete Class)
```

Interpretation:

* `Animal` defines required behavior
* `Dog` and `Cat` provide concrete implementations
* all subclasses share the same contract

---

### Duck Typing

In Python, objects are often used based on **what they can do**, not only on what they inherit from.

For example:

* if an object provides a method named `draw()`, it may be usable in a function that expects something drawable
* the object does not always need to inherit from a specific class for that use case

This approach is often called **duck typing**.

---

## General Requirements

All tasks in this project must follow these requirements unless otherwise specified.

### Environment

* Ubuntu 20.04
* Python 3.8

### Python Files

All Python files must:

* be executable
* start with:

```python
#!/usr/bin/env python3
```

### Coding Requirements

* All files must end with a newline
* Code must follow **PEP8**
* All modules, classes, and functions must include documentation strings
* Only the Python standard library may be used unless otherwise stated

---

# Tasks

## 0. Abstract Animal Class and its Subclasses

### Background

In object-oriented programming, Abstract Base Classes (ABCs) ensure that derived classes implement specific methods from the base class.

This provides a blueprint for creating and structuring derived classes.

Python's `ABC` package facilitates the creation of abstract base classes.

### Objective

1. Create an abstract class named `Animal` using the `ABC` package. This class must have an abstract method called `sound`.
2. Create two subclasses of `Animal`: `Dog` and `Cat`.
3. Implement the `sound` method in `Dog` so it returns the string `"Bark"`.
4. Implement the `sound` method in `Cat` so it returns the string `"Meow"`.

### Instructions

1. Import the necessary components from the `abc` module.
2. Define the `Animal` class so it inherits from `ABC`.
3. Inside `Animal`, declare an abstract method named `sound` using the `@abstractmethod` decorator.
4. Create a subclass named `Dog` that inherits from `Animal`.
5. Implement `sound` in `Dog` so it returns `"Bark"`.
6. Create a subclass named `Cat` that inherits from `Animal`.
7. Implement `sound` in `Cat` so it returns `"Meow"`.

### Hint

If a class still has abstract methods without implementation, Python will raise a `TypeError` when you try to instantiate it.

### Expected Structure

```text
             Animal
          (Abstract Class)
               │
        ┌──────┴──────┐
        ↓             ↓
       Dog           Cat
   sound() = Bark   sound() = Meow
```

### Example

```text
$ cat main.py
#!/usr/bin/env python3
from animals import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

animal = Animal()
print(animal.sound())

$ ./main.py
Bark
Meow
Traceback (most recent call last):
  File "main.py", line 10, in <module>
    animal = Animal()
TypeError: Can't instantiate abstract class Animal with abstract method sound
```

---

## Repository

**GitHub repository:**

`holbertonschool-core-engineering`

**Directory:**

`python_oop/abc`

**File:**

`animals.py`

---

## Resources

* Abstract Base Classes
* Python Tutorial — Classes
* Real Python — Python Interfaces
* Real Python — Mixins and Multiple Inheritance
* Geeks for Geeks — Abstract Classes in Python
