#!/usr/bin/python3
""" defines a file function """


def read_file(filename=""):
    """ a function that reads a text file
    and prints it to stdout
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read())
