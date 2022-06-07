#!/usr/bin/python3
""" Base class of all other classes in this project. Manage id attribute
in all future classes and avoid duplicating the same code.
"""


import json
import os


class Base:
    """the Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """the “base” of all other classes in this project
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string representation
        of list_dictionaries:
        """
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file
        """
        myfile = f"{cls.__name__}.json"
        with open(myfile, 'w', encoding="utf_8") as a:
            if list_objs is None or len(list_objs) == 0:
                return a.write(cls.to_json_string(None))
            mylist = []
            for elements in list_objs:
                mylist.append(elements.to_dictionary())
            jsn = cls.to_json_string(mylist)
            return a.write(jsn)

    @classmethod
    def create(cls, **dictionary):
        """class method returns an instance with all attributes already set.
        """
        dummy = 0
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        liste = []
        filename = f"{cls.__name__}.json"
        if os.path.exists(filename) is False:
            return []
        with open(filename, "r") as file:
            liste = cls.from_json_string(file.read())
            for i in range(len(liste)):
                liste[i] = cls.create(**liste[i])
        return liste
