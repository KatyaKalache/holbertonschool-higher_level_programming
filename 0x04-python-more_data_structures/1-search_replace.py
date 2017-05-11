#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list = my_list[:]
    list.remove(search)
    list.insert(search - 1, replace)
    return(list)
