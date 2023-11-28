#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div.
    Args:
        matrix: List of int or float
        div: number to divide

    Returns:
        list: List of divided matrix

    Raises:
        TypeError: When matrix is not list of lists containing float or int
        TypeError: When sublists are not all same size
        TypeError: When div is not float or int
        ZeroDivisionError: When div is zero
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for r in matrix:
        if not isinstance(r, list) or len(r) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(r) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for el in r:
            if not isinstance(el, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(el / div, 2) for el in r] for r in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")