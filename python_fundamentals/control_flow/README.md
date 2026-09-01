# Python - Control Flow

## Description

This project introduces control flow in Python.

Control flow allows a program to:

* execute different instructions depending on a condition;
* repeat instructions using loops;
* combine multiple logical conditions.

The project mainly covers:

* `if`
* `elif`
* `else`
* comparison operators;
* Boolean logic;
* `while` loops;
* `for` loops with `range()`.

## Objectives

By the end of the project, I should be able to:

* write conditions using `if`, `elif`, and `else`;
* correctly use comparison and logical operators;
* use `while` and `for` to repeat instructions;
* understand the limits and different iterations of a loop;
* produce formatted output;
* combine conditions and loops to obtain a deterministic result.

## Constraints

* Corrections are performed on Ubuntu 20.04 LTS.
* The Python version used is Python 3.8.x.
* Every Python file must begin exactly with:

```python
#!/usr/bin/env python3
```

* Every file must be executable.
* Every file must end with a newline.
* The code must comply with PEP8 using `pycodestyle 2.7.x`.
* No external libraries are allowed.
* No functions should be created in this project.
* No imports should be used.
* The output must exactly match the expected format.

## Resources

* Python Tutorial — Control Flow Tools
  https://docs.python.org/3/tutorial/controlflow.html

* Python Tutorial — More on Conditions
  https://docs.python.org/3/reference/expressions.html#comparisons

## Tasks

### 0. Positive anything is better than negative nothing

Create a script that assigns a random integer to a variable called `number`.

The program then uses conditions to print:

* `<number> is positive` if the number is greater than `0`;
* `<number> is zero` if the number is equal to `0`;
* `<number> is negative` if the number is less than `0`.

The structure used is:

```text
if

↓

elif

↓

else
```