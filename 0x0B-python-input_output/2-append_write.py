#!/usr/bin/python3
"""File reading function"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file
    (UTF8) and returns the number of characters added
    Args:
        filename: name of the file
        text: text to append
    Returns:
        number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
