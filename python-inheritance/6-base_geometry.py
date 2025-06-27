#!/usr/bin/python3
""" This module includes a class that  appends
more features to previous BaseGeometry class
by adding exception inside of it """


class BaseGeometry:
    """
    BaseGeometry class serves as a base for geometry shapes.
    """

    def area(self):
        """ Raises an exception with the
        message 'area() is not implemented' """

        raise Exception("area() is not implemented")
