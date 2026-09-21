#!/usr/bin/env python3


def read_file(filename=""):
    """Read a text file and print its content to stdout."""
    with open(filename)as f:
        print(f.read())
