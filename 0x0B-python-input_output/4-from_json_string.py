#!/usr/bin/python3
""" defines a text function """

import json


def from_json_string(my_str):
    """ a function that returns an object represnted by a JSON
    """
    return json.loads(my_str)
