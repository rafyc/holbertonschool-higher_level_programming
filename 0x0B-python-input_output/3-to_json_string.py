#!/usr/bin/python3
"""function that returns the JSON representation of an object (string):
"""
import json


def to_json_string(my_obj):
    """The to_json_string function

    Args:
        my_obj: string to convert in json.
    """
    return json.dumps(my_obj)
