#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """the append_write function

    Args:
        filename the file to write into.
        text to append.
    """
    with open(filename, 'a', encoding="utf_8") as myfile:
        return myfile.write(text)
