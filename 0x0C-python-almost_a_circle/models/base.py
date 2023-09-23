#!/usr/bin/python3
""" Base module"""
import json
import csv


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

    @staticmethod
    def from_json_string(json_string):
        """ a static method that returns
        the list of the JSON string
        representation json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ an Update to the class that
        returns an instance with all
        attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """a class method that returns a list of instances"""
        filename = cls.__name__ + ".json"
        instance_list = []
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                json_string = file.read()
                dict_list = cls.from_json_string(json_string)
                for dictionary in dict_list:
                    instance = cls.create(**dictionary)
                    instance_list.append(instance)
        except FileNotFoundError:
            pass
        return instance_list
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializing and saving to CSV file"""
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    data = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    data = [obj.id, obj.size, obj.x, obj.y]
                writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """deserializing and loading from CSV file"""
        filename = cls.__name__ + ".csv"
        instance_list = []
        try:
            with open(filename, mode="r", newline="") as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[1]), int(row[2]))
                        instance.id = int(row[0])
                        instance.x = int(row[3])
                        instance.y = int(row[4])
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[1]))
                        instance.id = int(row[0])
                        instance.x = int(row[2])
                        instance.y = int(row[3])
                    instance_list.append(instance)
        except FileNotFoundError:
            pass
        return instance_list
