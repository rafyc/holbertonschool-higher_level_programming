#!/usr/bin/python3
"""
Write a function that returns the dictionary description
with simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""


def class_to_json(obj):
    """The class_tà_json

    Args:
        obj: the object to convert
    """
    return obj.__dict__
