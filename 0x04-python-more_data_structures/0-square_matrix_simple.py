#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = []
    for row in matrix:
        squares.append([i*i for i in row])
    return squares
