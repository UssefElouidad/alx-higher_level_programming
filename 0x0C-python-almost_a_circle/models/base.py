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

    @classmethod
    def save_to_file(cls, list_objs):
        """a class method that writes the JSON
        string representation of list_objs to
        a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as file:
            d_list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(d_list)
            file.write(json_string)
