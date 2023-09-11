#!/usr/bin/python3
""" defines a class checking function """


def is_same_class(obj, a_class):
    """ a function that returns
    True if the objest is exactly
    an instance of the specified class
    """
    return type(obj) is a_class
