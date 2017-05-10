#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for rows in matrix:
        for cols in rows:
            print("{:d}".format(cols), end="")
            if cols % 3 != 0:
                print(" ", end="")
        print("")
