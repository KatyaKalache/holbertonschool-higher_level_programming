#!/usr/bin/python3
def update_dictionary(my_dict, key, value):
    new_dict = my_dict.copy()
    new_dict[key] = value
    return new_dict
