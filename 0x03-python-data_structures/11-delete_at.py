#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list is not None or my_list != []:
        del (my_list[idx])
        return  my_list
    else:
        return None
