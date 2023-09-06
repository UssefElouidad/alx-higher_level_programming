#!/usr/bin/python3
""" an empty class recangle"""


class Rectangle:
    """ this class is for a real rectangle
    width is the wisth of the rectangle
    highit id the hight of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

        @property
        def width(self):
            return self.width

        @width.setter
        def width(self, value):
            if not isinstance(x, (int)):
                raise TypeError("width must be an integer")
            if width < 0:
                raise ValueError("width must be >= 0")
            self.width = value

        @property
        def height(self):
            return self.height

        @height.setter
        def height(self, value):
            if not isinstance(x, (int)):
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")
            self.width = value

