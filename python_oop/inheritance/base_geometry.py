#!/usr/bin/env python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """Base class for geometric shapes."""

    def area(self):
        """Raise an exception, because area is not implemented here."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check that value is an integer greater than 0.

        Args:
            name (str): the name of the value, used in error messages.
            value: the value to check.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
