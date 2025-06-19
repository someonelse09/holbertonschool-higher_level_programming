#!/usr/bin/python3
def max_integer(my_list=[]):
    if(len(my_list) == 0):
        return None
    M = my_list[0]
    for j in range(1, len(my_list)):
        if my_list[j] > M:
            M = my_list[j]
    return M
