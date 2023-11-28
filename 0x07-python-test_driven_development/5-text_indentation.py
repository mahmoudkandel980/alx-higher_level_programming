#!/usr/bin/python3
"""text_indentation method"""


def text_indentation(text):
    """adding two new lines after '.?:' chars.

    Args:
        text: string

    Raises:
        TypeError: When text is not a str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for one in ".?:":
        text = (one + "\n\n").join(
            [line.strip(" ") for line in text.split(one)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")