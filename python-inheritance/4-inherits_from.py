#!/usr/bin/python3
""" This module includes a function
named inherits_from that checks
whether the object is inherited from given class or not """


def inherits_from(obj, a_class):
    """ This function returns True if
    obj is inherited from a_class and False otherwise """

    return issubclass(obj, a_class)
