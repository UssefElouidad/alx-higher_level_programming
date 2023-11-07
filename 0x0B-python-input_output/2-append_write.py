#!/usr/bin/python3
""" defines a text function"""


def append_write(filename="", text=""):
    """  a function that appends a string
    at the end of a text file
    and returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        chars_added = f.write(text)
    return chars_added
