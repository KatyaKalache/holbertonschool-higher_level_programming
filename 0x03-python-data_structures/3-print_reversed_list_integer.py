#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not 0:
        my_list.sort(reverse=True)
        for i in my_list:
            print("{:d}".format(i))
