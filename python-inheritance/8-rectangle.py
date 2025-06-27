#!/usr/bin/python3
""" This module defines a class
called Rectangle that is inherited
from BaseGeometry class which
has been created in the previous task """


class Rectangle(BaseGeometry):
    """ This class includes init method and
    attributes width and height that are validated """

    def __init__(self, width, height):
        """
        Initializes a Rectangle with validated private width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """

        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height
