#!/usr/bin/python3
""" This module creates a rectangle class
for geometric rectangle representation """


class Rectangle:
    """ This class  defines a Rectangle
    and methods for its parameters: height and width
    """

    def __init__(self, width=0, height=0):
        """ This is the initialization of the
        Rectangle class in order for us to generate an object from it """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ This method allows us to get
        the value of Rectangle's width """
        return self.__width
    @width.setter

    def width(self, value):
        """ This method serves as a width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ This method is for getting
        the value of Rectangle's height """
        return self.__height

    @height.setter
    def height(self, value):
        """ This method is defined for 
        setting a new value for the height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
