#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for key, value in sorted(my_dict.items()):
        s = ("{:s} : {}".format(key, value))
        print(s)
