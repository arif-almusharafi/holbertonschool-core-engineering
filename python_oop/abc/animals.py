#!/usr/bin/env python3
"""Module that defines an abstract Animal class and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal."""
        pass


class Dog(Animal):
    """Dog class, a concrete subclass of Animal."""

    def sound(self):
        """Return the sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Cat class, a concrete subclass of Animal."""

    def sound(self):
        """Return the sound of a cat."""
        return "Meow"
