#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for row in matrix:
        print(" ".join("{:d}".format(cols) for cols in row))
