#!/usr/bin/python3
""" This module defines a class MyList
that inherits from a list and has a method
that returns sorted version of the list """


class MyList(list):
    """ This class inherits from
    another class called list """

    def print_sorted(self):
        """ This method sorts the list
        in ascending order """
        print(sorted(self))
