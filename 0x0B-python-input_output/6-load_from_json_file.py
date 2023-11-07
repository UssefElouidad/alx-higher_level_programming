#!/usr/bin/python3
""" defines a text function """


import json


def load_from_json_file(filename):
    """ a function that creates an object to a text file
    using a JSON represntation
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
