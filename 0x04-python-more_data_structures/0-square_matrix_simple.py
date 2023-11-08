#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    for r in matrix:
        trans = []
        for el in r:
            el = el * el
            trans.append(el)
        newMatrix.append(trans)
    return newMatrix
