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

    def integer_validator(self, name, value):
        """ This method allows us to validate
        the value is positive integer with the assumption
        that name is always is a string being hold """

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
