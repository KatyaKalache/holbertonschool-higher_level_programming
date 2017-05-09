#!/usr/bin/python3
def element_at(my_list, idx):
    if idx <= len(my_list):
        return ('{:d}'.format(my_list[idx]))
    if idx < 0:
        return None
