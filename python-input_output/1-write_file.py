#!/usr/bin/python3
""" This module contains a function that
has permission to write the file """


def write_file(filename="", text=""):
    """ This function uses write, open functions
    and with statement in order to write it """

    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text) - 2
