#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = my_dict.copy()
    new_dict.update((i, age*2) for i, age in new_dict.items())
    return new_dict
