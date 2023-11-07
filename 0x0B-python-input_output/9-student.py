#!/usr/bin/python3
''' creation of the student class '''


class Student:
    ''' representation of a student'''
    def __init__(self, first_name, last_name, age):
        ''' inisializasyion '''
        self.first_name = first_name
        self.last_name = last_name
        self. age = age

    def to_json(self):
        ''' returns a dictionnary that represents a student'''
        return self.__dict__
