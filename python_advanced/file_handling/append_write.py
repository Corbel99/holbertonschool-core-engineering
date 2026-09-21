#!/usr/bin/env python3
"""Module for appending text to a file."""


def write_file(filename="", text=""):
    """Append a string to a text file and return
    the number of characters added."""
    with open(filename, "a")as f:
        return f.write(text)
