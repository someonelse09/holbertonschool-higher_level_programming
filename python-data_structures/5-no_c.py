#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for x in my_string:
        if x == 'c' or x == 'C':
            continue
        else:
            new_string += x
    return new_string
