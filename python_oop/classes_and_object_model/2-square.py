#!/usr/bin/env python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size = 0):
        """Initializes a square with a given size."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
