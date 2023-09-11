#!/usr/bin/python3
""" defines a class checker function """


def inherits_from(obj, a_class):
    return issubclass(type(obj), a_class) and type(obj) is not a_class
