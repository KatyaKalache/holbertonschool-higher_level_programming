#!/usr/bin/python3
def simple_delete(my_dict, key=""):
    new_dict = my_dict
    if key in new_dict:
        del new_dict[key]
        return new_dict
    else:
        return my_dict
