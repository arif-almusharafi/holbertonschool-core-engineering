#!/usr/bin/env python3
"""Module that defines the Square class."""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Square defined by its size, based on the Rectangle class."""

    def __init__(self, size):
        """Set the size after validating it.

        Args:
            size (int): the length of each side of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
