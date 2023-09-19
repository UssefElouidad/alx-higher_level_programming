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

    def update(self, *args, **kwargs):
        """ public method that assigns attributes """
        num_args = len(args)

        if num_args >= 1:
            self.id = args[0]
        if num_args >= 2:
            self.width = args[1]
        if num_args >= 3:
            self.x = args[2]
        if num_args >= 4:
            self.y = args[3]

        if num_args == 0 or num_args < 4:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """Return a string representation of the Square instance."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    #def to_dictionary(self):
        """ a public method that returns the dictionary
        representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "heghit": self.heghit,
            "x": self.x,
            "y": self.y,
            }
