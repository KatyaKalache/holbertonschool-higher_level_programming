#!/usr/bin/python3
def update_dictionary(my_dict, key, value):
    key = key.replace(" ", "")
    my_dict[key] = value
    return my_dict
