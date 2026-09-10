#!/usr/bin/env python3
"""
This module defines Fish, Bird, and FlyingFish classes.
"""


class Fish:
    """
    Represents a fish.
    """

    def swim(self):
        """
        Make the fish swim.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Describe the habitat of the fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Represents a bird.
    """

    def fly(self):
        """
        Make the bird fly.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Describe the habitat of the bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a fish that can fly.
    """

    def fly(self):
        """
        Make the flying fish soar.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Make the flying fish swim.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Describe the habitat of the flying fish.
        """
        print("The flying fish lives both in water and the sky!")


flyingfish = FlyingFish()

flyingfish.fly()
flyingfish.swim()
flyingfish.habitat()

print(FlyingFish.mro())
