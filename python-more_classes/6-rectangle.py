#!/usr/bin/python3
""" This module creates a rectangle class
for geometric rectangle representation """


class Rectangle:
    """ This class  defines a Rectangle
    and methods for its parameters: height and width
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ This is the initialization of the
        Rectangle class in order for us to generate an object from it """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        self.__height = value

    def area(self):
        """ This method calculates
        the area of the Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ This method returns perimeter
        based on the size of the Rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2*(self.__height + self.__width)

    def __str__(self):
        """ This method prints the
        Rectangle object using hash symbol """
        if self.__height == 0 or self.__width == 0:
            return ""
        repictangle = ""
        for i in range(self.__height):
            for j in range(self.__width):
                repictangle += "#"
            if i < self.__height - 1:
                repictangle += "\n"
        return repictangle

    def __repr__(self):
        """ This method serves us to
        represent the official string version """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ This method prints a message
        when an object of Rectangle class is deleted """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
