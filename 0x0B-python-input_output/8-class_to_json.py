#!/usr/bin/python3
''' contains the class_to_json function '''


def class_to_json(obj):
    ''' a class that returns the dictionarry description
    with simple data structure
    for JSON serialization of an object '''
    return obj.__dict__
