# Python - File Handling

## Description

This project introduces Python's input/output mechanisms with a focus on file manipulation.

The goal is to learn how Python programs can interact with files to read external data, write information, and preserve data beyond the execution of a program.

The project also introduces the importance of properly managing file resources, particularly through the use of the `with` statement.

## Learning Objectives

At the end of this project, you should be able to:

* Open a file
* Write text to a file
* Read the full content of a file
* Read a file line by line
* Move the cursor in a file
* Make sure a file is properly closed after use
* Understand and use the `with` statement

## Resources

The project is based on the following resources:

* Python documentation — Reading and Writing Files
* Python documentation — Predefined Clean-up Actions
* *Dive Into Python 3*, Chapter 11 — Files, until and including "11.4 Binary Files"
* *Learn to Program 8* — Reading / Writing Files

## Requirements

* All files are interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
* All files must end with a new line
* The first line of every Python file must be exactly:
  `#!/usr/bin/env python3`
* A `README.md` file is mandatory at the root of the project
* Code must follow pycodestyle 2.7.*
* All files must be executable
* File length is tested using `wc`

## Directory

```text
python_advanced/
└── file_handling/
    ├── README.md
    ├── read_file.py
    └── ...
```

## Concepts

The project covers the fundamental operations required to work with files in Python:

```text
open()
   ↓
file object
   ↓
read / write
   ↓
resource management
   ↓
with
```

These concepts provide the foundations for working with external data and will support future work involving data processing and other forms of input/output.
