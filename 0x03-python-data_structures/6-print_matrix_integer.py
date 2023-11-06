i#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for matrixRow in matrix:
        for matrixCol in matrixRow:
            print("{:d}".format(matrixCol), end=" " if matrixCol != matrixRow[-1] else "")
        print()
