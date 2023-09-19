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
    def width(self):
        """Getter method for width"""
        return self.__width
    @width.setter
    def width(self, value):
        """ setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height"""
        return self.__height
    @height.setter
    def height(self, value):
        """ setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter for x"""
        return self.__x
    @x.setter
    def x(self, value):
        """setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >=0")
        self.__x = value

    @property
    def y(self):
        """ getter for y"""
        return self.__y
    @y.setter
    def y(self, value):
        """ setter for y"""
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
    def update(self, *args, **kwargs):
        """ update the attributes of the rectangle with arguments"""
        num_arg = len(args)
        if num_arg >= 1:
            self.id = args[0]
        if num_arg >= 2:
            self.width = args[1]
        if num_arg >= 3:
            self.height = args[2]
        if num_arg >= 4:
            self.__x = args[3]
        if num_arg >= 5:
            self.__y = args[4]

        if num_arg == 0 or num_arg < 5:
            for key, value in kwargs.items():
                setattr(self, key, value)
