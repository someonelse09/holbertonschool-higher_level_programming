#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    res = sorted(a_dictionary)
    for x in res:
        print("{}: {}".format(x, a_dictionary.get(x)))
