#!/usr/bin/python3


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initiate an instance of the Square class"""
        self.__size = size

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size
    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Return the area of the square"""
        return(self.__size * self.__size)

    def my_print(self):
        """Print out square"""
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end='')
            print()
