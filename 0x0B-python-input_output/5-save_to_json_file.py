#!/usr/bin/python3
""" defines a text function """
import json


def save_to_json_file(my_obj, filename):
    """ a function that writes an object to a text file
    using a JSON represntation
    """
    with open(filename, "w" , encoding="utf-8") as f:
        json.dump(my_obj, f)
