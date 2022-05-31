#!/usr/bin/python3
"""function that creates an Object from a “JSON file”:
"""

import json


def load_from_json_file(filename):
    """The loads_from_json_file function

    Args:
        filename the file to create the object from.
    """
    with open(filename, 'r', encoding="utf_8") as myfile:
        return json.load(myfile)
