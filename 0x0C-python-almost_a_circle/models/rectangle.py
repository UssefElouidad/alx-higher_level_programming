#!/usr/bin/python3
""" Rectangle module """

from models.base import Base

class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initilise rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    """ getter for width"""
    def width(self):
        return self.__width
    @width.setter
    """ setter for width"""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    """ getter for height"""
    def height(self):
        return self.__height
    @height.setter
    """ setter for height"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    """ getter for x """
    def x(self):
        return self.__x
    @x.setter
    """setter for x"""
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >=0")
        self.__x = value

    @property
    """ getter for y"""
    def y(self):
        return self.__y
    @y.setter
    """ setter for y"""
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= o")
        self.__y = value
    def area(self):
        return self.width * self.height
    def display(self):
        """ Return a string representation of the rectangle using # characters """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
