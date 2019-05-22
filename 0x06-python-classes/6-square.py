#!/usr/bin/python3


class Square:
    """Class that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initiate an instance of the Square class"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the position attribute of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position as a tuple of the square"""
        if (type(value) != tuple or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) != int or type(value[1]) != int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Return the area of the square"""
        return(self.__size * self.__size)

    def my_print(self):
        """Print out square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end='')
                for i in range(self.__size):
                    print("#", end='')
                print()
