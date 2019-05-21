#!/usr/bin/python3


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initiate an instance of the Square class"""
        self.set_size(size)

    def get_size(self):
        """Get the size of the square"""
        return self.__size

    def set_size(self, size):
        """Set the size of the square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return the area of the square"""
        return(self.__size * self.__size)
