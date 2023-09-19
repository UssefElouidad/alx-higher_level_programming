#!/usr/bin/python3
""" class Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class."""
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize a square instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
         """ public method that assigns attributes """
         if args:
             super().update(*args)
         elif kwargs:
             super().update(**kwargs)

