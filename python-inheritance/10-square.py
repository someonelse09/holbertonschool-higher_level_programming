#!/usr/bin/python3
"""
This module defines the Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    Validates size using integer_validator.
    """

    def __init__(self, size):
        """
        Initializes a Square with validated private size.

        Args:
            size (int): The size of the square's sides.
        """

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.
        """

        return self.__size * self.__size

