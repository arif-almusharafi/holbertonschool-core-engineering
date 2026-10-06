#!/usr/bin/env python3
"""Module that writes text to a file."""


def write_file(filename="", text=""):
    """write a string to a UTF8 text file."""
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(text)
