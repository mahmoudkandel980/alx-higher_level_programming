#!/usr/bin/python3

"""Defines a file-appending function."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing a specific string.

    Args:
        filename: the name of the file
        search_string: the string to search for
        new_string: the string to insert
    """
    txt = ""
    with open(filename) as r:
        for line in r:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
