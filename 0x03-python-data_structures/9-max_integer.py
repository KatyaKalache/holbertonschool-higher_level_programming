#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        my_list.sort();
        my_list.reverse();
        max = my_list[0]
        return max
