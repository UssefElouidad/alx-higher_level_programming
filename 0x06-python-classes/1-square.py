#!/usr/bin/python3
""" Define a class square """


class Square:
    """ Represent a square """
    def __init__(self, size):
        """
        Constructor for square class.
        Args:
            size(int) the size to assign to the square.
        """
        self._Square__size = size
    def get_size(self):
        """
        gets the size of the square
        Returns:
        int: the size of the square
        """
        return self.size
