#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    for i in matrix:
        sq = map(lambda j: j*j, i)
    return sq
