#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    dif1 = tuple(set(set_1) - set(set_2))
    dif2 = tuple(set(set_2) - set(set_1))
    dif = dif1 + dif2
    return dif
