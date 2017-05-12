#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for key, element in sorted(my_dict.items()):
        s = ("{:s} : {}".format(key, element))
        print(s)
