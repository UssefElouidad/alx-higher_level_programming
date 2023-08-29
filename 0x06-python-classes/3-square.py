#!/usr/bin/python3
""" Define a class square """


class Square:
    """ Represent a square """
    def __init__(self, size=0):
        """
        Constructor for square class.
        Args:
            size(int) the size to assign to the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    def get_size(self):
        """
        gets the size of the square
        Returns:
        int: the size of the square
        """
        return self.size

    def area(self):
        """
        Calculation and return the area of the square.
        Returns:
            int: the area of the square.
        """
        return self._Square__size * self._Square__size

