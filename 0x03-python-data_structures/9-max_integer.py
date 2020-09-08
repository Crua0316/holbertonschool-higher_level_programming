#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    i_max = my_list[0]
    for a in range(len(my_list)):
        if my_list[a] > i_max:
            i_max = my_list[a]
    return i_max
