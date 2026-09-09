#!/usr/bin/env python3
"""Defines the BaseGeometry class."""


class BaseGeometry:
    """Represents the base geometry."""

    def area(self):
        """Calculate the area of the geometry."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
