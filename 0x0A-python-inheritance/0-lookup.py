#!/usr/bin/python3
def lookup(obj):
    """ a function that returns
    the list of available attributes
    and methodes of an object
    """
    attributes_and_methods = dir(obj)
    result_list = []
    for item in attributes_and_methods:
        result_list.append(item)
    print(result_list)
