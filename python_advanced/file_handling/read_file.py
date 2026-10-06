#!/usr/bin/env python3
"""Module that writes text to a file."""


def read_file(filename=""):
    """Reads a UTF8 text file and prints it to stdout."""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
