#!/usr/bin/python3


class Square:
    """Class that defines a square"""

    def __init__(self, size=0):
        """Initiate an instance of the Square class"""
        self.__size = size

    def __str__(self):
        """compute the “official” string representation of an object."""
        return(str(self.__size))

    def __lt__(self, other):
        """compare one object number with the other object number"""
        return(self.__size < other.__size)

    def __le__(self, other):
        """compare one object number with the other object number"""
        return(self.__size <= other.__size)

    def __eq__(self, other):
        """compare one object number with the other object number"""
        return(self.__size is other.__size)

    def __ne__(self, other):
        """compare one object number with the other object number"""
        return(self.__size is not other.__size)

    def __ge__(self, other):
        """compare one object number with the other object number"""
        return(self.__size >= other.__size)

    def __gt__(self, other):
        """compare one object number with the other object number"""
        return(self.__size > other.__size)

    @property
    def size(self):
        """Get the size of the square"""
        return(self.__size)

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
