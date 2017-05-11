#!/usr/bin/python3
def uniq_add(my_list=[]):
    myset = set(my_list)
    b = 0
    for a in myset:
        b = a + b
    return(b)
