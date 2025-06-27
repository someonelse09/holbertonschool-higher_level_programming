#!/usr/bin/python3
"""
This module defines the Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    Validates width and height using integer_validator.
    Implements area() and __str__().
    """

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

    def area(self):
        """
        Returns the area of the rectangle.
        """

        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle.
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
