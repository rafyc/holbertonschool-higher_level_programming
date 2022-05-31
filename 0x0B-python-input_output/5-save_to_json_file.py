#!/usr/bin/python3
""" function that writes an Object to a text file,
 using a JSON representation:
"""

import json


def save_to_json_file(my_obj, filename):
    """    with open(filename, 'w', encoding="utf_8") as myfile:
        return myfile.write(json.dumps(my_obj))
    Returns:
        _type_: _description_
    """
    with open(filename, 'w', encoding="utf_8") as myfile:
        return myfile.write(json.dumps(my_obj))
