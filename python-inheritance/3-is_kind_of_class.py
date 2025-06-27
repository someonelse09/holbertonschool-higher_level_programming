#!/usr/bin/python3
""" This module includes a function
named is_kind_of_class that checks
whether the object is of the given type or not """


def is_kind_of_class(obj, a_class):
    """ This function returns True
    if obj is a type of a_class and False otherwise """

    return isinstance(obj, a_class)
