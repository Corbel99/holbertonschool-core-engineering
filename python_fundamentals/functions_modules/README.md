# Python - Functions & Modularity

## Introduction

As programs grow, repeating logic becomes inefficient and error-prone.

**Functions** allow you to encapsulate behavior into reusable blocks.

**Modules** allow you to organize those functions into separate files and reuse them safely.

This project introduces:

* Function definition and return values
* Execution flow inside and outside functions
* Separation between printing and returning
* How Python executes a file
* How importing a file affects execution
* How to reuse functions and variables across files

The order of the exercises is intentional. The project progresses from defining functions to safely organizing code across multiple files.

---

## Learning Objectives

By the end of this project, you should be able to:

* Define functions with parameters and return values.
* Distinguish clearly between `print` and `return`.
* Implement logic inside functions using conditionals and loops.
* Understand how Python executes top-level code in a file.
* Explain what `if __name__ == "__main__"` does and why it is necessary.
* Import functions from other files.
* Import variables from other files.
* Write scripts that behave correctly when executed and when imported.

---

## Resources

* Python Tutorial — Defining Functions
  https://docs.python.org/3/tutorial/controlflow.html#defining-functions

* Python Tutorial — Modules
  https://docs.python.org/3/tutorial/modules.html

* Python Reference — `__name__`
  https://docs.python.org/3/library/__main__.html

* PEP8 Style Guide
  https://peps.python.org/pep-0008/

---

## General Requirements

Corrections will run on:

* **Ubuntu 20.04 LTS**
* **Python 3.8.x**

The first line of every Python file must be exactly:

```python
#!/usr/bin/env python3
```

All files must:

* Be executable.
* End with a newline.
* Be PEP8 compliant using `pycodestyle 2.7.x`.

No external libraries are allowed.

No use of `sys.argv` is allowed in this project.

Each task must follow its own constraints precisely.

---

# Tasks

## 0. islower

### Objective

Write a function:

```python
def islower(c):
```

The function must return:

* `True` if `c` is a lowercase letter.
* `False` otherwise.

### Constraints

* You are not allowed to use built-in string methods such as `.islower()`.
* You must use ASCII logic with `ord()`.
* The function must return a boolean value.

### Examples

```python
>>> islower('a')
True
>>> islower('A')
False
>>> islower('3')
False
```

### Repository

**GitHub repository:**

`holbertonschool-core-engineering`

**Directory:**

`python_fundamentals/functions_modules`

**File:**

`islower.py`

---

## Project Progression

The exercises progressively cover:

```text
Function definition
        ↓
Parameters
        ↓
Return values
        ↓
print vs return
        ↓
Conditionals and loops
        ↓
Python file execution
        ↓
__name__ == "__main__"
        ↓
Importing functions
        ↓
Importing variables
        ↓
Modularity
```

The overall goal is to understand how to write reusable functions and how to properly organize Python code across multiple files.
