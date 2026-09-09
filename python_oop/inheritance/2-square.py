#!/usr/bin/env python3
"""Defines the Square class that inherits from Rectangle."""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""
    def __init__(self, size):
        """Initialize a Square instance with size."""
        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the square."""
        return f"[Square] {self.__size}/{self.__size}"
