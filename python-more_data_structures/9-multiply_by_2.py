#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict(map(lambda x: (x, a_dictionary[x]*2), a_dictionary))
    return new_dict
