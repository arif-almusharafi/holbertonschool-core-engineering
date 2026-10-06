#!/usr/bin/env python3
"""Module that append text to a file."""


def append_write(filename="", text=""):
    """append to the end of the file """
    with open(filename, "a" ,encoding="UTF-8") as f:
        return f.write(text)
