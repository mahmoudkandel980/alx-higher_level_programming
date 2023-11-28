#!/usr/bin/python3
"""say_my_name method"""


def say_my_name(first_name, last_name=""):
    """printing first && last name.

    Args:
        first_name: first name
        last_name: last name

    Raises:
        TypeError: If first name or last name are not string
    """
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")