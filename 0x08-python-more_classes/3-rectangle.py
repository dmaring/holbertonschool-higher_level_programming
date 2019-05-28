#!/usr/bin/python3
"""
Simple rectangle module
"""


class Rectangle:
    """Class that represents a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return(self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return(0)
        else:
            return((2 * self.width) + (2 * self.height))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return("")
        ret_string = ""
        for row in range(self.height):
            for col in range(self.width):
                ret_string += ("#")
            if row < self.height - 1:
                ret_string += ("\n")
        return(ret_string)
