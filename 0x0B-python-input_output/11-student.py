#!/usr/bin/python3
"""
Write a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """a class Student that defines a student by:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        """

        try:
            return {i: self.__dict__[i] for i in attrs if i in self.__dict__}

        except TypeError:
            return self.__dict__

    def reload_from_json(self, json):
        for attribute in json:
            self.__dict__[attribute] = json[attribute]
