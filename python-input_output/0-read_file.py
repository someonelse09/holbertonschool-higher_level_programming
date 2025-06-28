#!/usr/bin/python3
""" This module contains a function that
gets permission to read the file """


def read_file(filename=""):
    """ This function uses read functions
    and with statement in order to read it """

    with open(filename) as f:
        print(f.read())
