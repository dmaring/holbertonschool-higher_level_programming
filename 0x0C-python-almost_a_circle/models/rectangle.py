"""
This module contains the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """A class that represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def check_int(self, str_obj, value):
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(str_obj))

    def check_gr_0(self, str_obj, value):
        if value <= 0:
            raise ValueError('{} must be > 0'.format(str_obj))

    def check_gr_eq_0(self, str_obj, value):
        if value < 0:
            raise ValueError('{} must be >= 0'.format(str_obj))

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        self.check_int('width', value)
        self.check_gr_0('width', value)
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        self.check_int('height', value)
        self.check_gr_0('height', value)
        self.__height = value

    @property
    def x(self):
        return(self.__x)

    @x.setter
    def x(self, value):
        self.check_int('x', value)
        self.check_gr_eq_0('x', value)
        self.__x = value

    @property
    def y(self):
        return(self.__y)

    @y.setter
    def y(self, value):
        self.check_int('y', value)
        self.check_gr_eq_0('y', value)
        self.__y = value
