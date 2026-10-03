#!/usr/bin/env python3
"""Module that shows multiple inheritance with Fish, Bird and FlyingFish."""


class Fish:
    """Fish class."""

    def swim(self):
        """Print how the fish moves."""
        print("The fish is swimming")

    def habitat(self):
        """Print where the fish lives."""
        print("The fish lives in water")


class Bird:
    """Bird class."""

    def fly(self):
        """Print how the bird moves."""
        print("The bird is flying")

    def habitat(self):
        """Print where the bird lives."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class, inherits from both Fish and Bird."""

    def fly(self):
        """Print how the flying fish flies."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print how the flying fish swims."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print where the flying fish lives."""
        print("The flying fish lives both in water and the sky!")
