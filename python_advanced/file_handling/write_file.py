#!/usr/bin/env python3
"""Module for writing text to a file."""


def write_file(filename="", text=""):
    """Write a string to a text file and
    return the number of characters written."""
    with open(filename, "w")as f:
        return f.write(text)
