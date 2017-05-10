#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = 0
    for i, val in enumerate(my_list):
        if val > max_int:
            max_int = val
    return max_int
