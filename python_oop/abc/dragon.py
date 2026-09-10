#!/usr/bin/env python3
"""
This module defines mixins for swimming and flying behaviors,
and a Dragon class that combines them.
"""


class SwimMixin:
    """
    Mixin that provides swimming behavior.
    """

    def swim(self):
        """
        Make the creature swim.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin that provides flying behavior.
    """

    def fly(self):
        """
        Make the creature fly.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Represents a dragon that can swim, fly, and roar.
    """

    def roar(self):
        """
        Make the dragon roar.
        """
        print("The dragon roars!")


dragon = Dragon()

dragon.swim()
dragon.fly()
dragon.roar()
