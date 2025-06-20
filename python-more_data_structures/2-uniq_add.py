#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    s = set(my_list)
    for i in s:
        sum = sum + i
    return sum
