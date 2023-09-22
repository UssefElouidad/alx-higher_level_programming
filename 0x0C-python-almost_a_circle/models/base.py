#!/usr/bin/python3
""" Base module"""
import json


class Base:
    """ Base class Updated by adding
    a static method that returns
    the JSON string representation
    of list_dictionaries"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ the method that converts the list
        of dictionaries to a JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
