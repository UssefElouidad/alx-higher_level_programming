#!/usr/bin/python3
""" defines a file function """


def write_file(filename="", text=""):
    """ a function that writes a string to a text file
    and returns the number of carachters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        chars_written = file.write(text)
        return chars_written
