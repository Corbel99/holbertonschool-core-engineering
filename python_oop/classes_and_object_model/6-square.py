#!/usr/bin/env python3
"""Defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with a given size and position."""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        self.position = position

    def area(self):
        """Calculates the area of the square."""

        return self.__size ** 2

    @property
    def position(self):
        """Getter for the position of the square."""

        return self.__position

    @position.setter
    def position(self, value):
        """Setter for the position of the square."""

        if (
            not isinstance(value, tuple) or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0 or value[1] < 0
        ):

            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """Getter for the size of the square."""

        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of the square."""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints the square using the '#' character."""

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print(self.position[0] * " " + "#" * self.__size)

    def __str__(self):
        """Returns a string representation of the square."""

        if self.__size == 0:
            return ""
        else:
            result = ""
            for i in range(self.size):
                result += self.position[0] * " " + "#" * self.size
                if i != self.size - 1:
                    result += "\n"
            return result
