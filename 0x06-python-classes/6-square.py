#!/usr/bin/python3
""" Define a class square """


class Square:
    """ Represent a square """
    def __init__(self, size=0, position=(0, 0)):
        """
        Constructor for square class.
        Args:
            size(int) the size to assign to the square.
        """
        self._Square__size = size
        self._position = position

    @property
    def size(self, value):
        """
        gets the size of the square
        Returns:
        int: the size of the square
        """
        return self._Square__size

    @size.setter
    def size(self, value):
        """
        sets the value of the square size.
        Returns:
        the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    @property
    def position(self):
        """
        Getter method to retrieve the position.
        """
        return self._position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            not all(i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value
    def area(self):
        """
        Calculation and return the area of the square.
        Returns:
            int: the area of the square.
        """
        return self._Square__size * self._Square__size

    def my_print(self):
        """
        Print the square with # character
        """
        if self._Square__size == 0:
            print()
        else:
            for _ in range(self._position[1]):
                print()
            for _ in range(self._Square__size):
                print(" " * self._position[0] + "#" * self._Square__size)
