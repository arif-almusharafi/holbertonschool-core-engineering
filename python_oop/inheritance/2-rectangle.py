#!/usr/bin/env python3
"""Module that defines the Rectangle class with area and string output."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle defined by a width and a height."""

    def __init__(self, width, height):
        """Set the width and height after validating them.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the description: [Rectangle] <width>/<height>."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
