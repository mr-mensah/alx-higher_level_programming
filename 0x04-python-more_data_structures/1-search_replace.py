#!/usr/bin/python3
def search_replace(my_list, search, replace):
    free_list = []
    for i in my_list:
        if i == search:
            free_list.append(replace)
        else:
            free_list.append(i)
    return free_list
