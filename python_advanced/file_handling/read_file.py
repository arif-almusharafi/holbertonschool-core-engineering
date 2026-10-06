#!/usr/bin/env python3
"""Module that writes text to a file."""


def read_file(filename=""):
    """Writes a string to a UTF8 text file."""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
