#!/usr/bin/python3
""" defines a class that inherits froom a list"""


class MyList(list):
    """ a public instance
    that prints the list
    but soted
    """
    def print_sorted(self):
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
