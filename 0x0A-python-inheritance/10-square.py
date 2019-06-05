#!/usr/bin/python3
"""
Module that holds square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class for Square"""

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return(self.__size * self.__size)
