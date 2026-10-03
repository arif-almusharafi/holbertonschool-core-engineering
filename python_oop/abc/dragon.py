#!/usr/bin/env python3
"""Module that shows how to use mixins with a Dragon class."""


class SwimMixin:
    """Mixin that adds the swim ability."""

    def swim(self):
        """Print that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds the fly ability."""

    def fly(self):
        """Print that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class, built from SwimMixin and FlyMixin."""

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
