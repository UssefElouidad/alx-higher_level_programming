#!/usr/bin/python3
""" defines an empty class"""


class BaseGeometry:
    """ an empty class
    """
    def area(self):
        ''' a way to copute area. '''
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        ''' away to validate value. '''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

