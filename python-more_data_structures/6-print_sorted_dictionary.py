#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l = sorted(a_dictionary)
    for x in l:
        print("{}: {}".format(x, a_dictionary.get(x)))
