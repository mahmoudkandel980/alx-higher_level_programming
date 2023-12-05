#!/usr/bin/python3
"""File reading function"""


def read_file(filename=""):
    """Prints UTF8 contents of a file to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
