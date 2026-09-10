#!/usr/bin/env python3

"""This module defines an abstract base class for animals."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals.
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses to make a sound.
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal.
    """

    def sound(self):
        """
        Implementation of the sound method for Dog.
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal.
    """

    def sound(self):
        """
        Implementation of the sound method for Cat
        """
        return "Meow"
