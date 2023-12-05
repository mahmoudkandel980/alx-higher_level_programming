#!/usr/bin/python3

"""
This is a module docstring"""


def pascal_triangle(n):
    """
    This is a function docstring

    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        triangle = triangles[-1]
        k = [1]
        for i in range(len(triangle) - 1):
            k.append(triangle[i] + triangle[i + 1])
        k.append(1)
        triangles.append(k)
    return triangles
