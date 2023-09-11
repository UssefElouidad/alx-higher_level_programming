#!/usr/bin/python3
""" defines an object attribute lookup function """


def lookup(obj):

    """ a function that returns
    the list of available attributes
    and methodes of an object
    """
    attributes_and_methods = dir(obj)
    return attributes_and_methods
