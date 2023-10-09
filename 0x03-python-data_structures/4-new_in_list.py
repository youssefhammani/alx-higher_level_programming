#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tmp_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return(my_list)
    tmp_list[idx] = element
    return(tmp_list)
