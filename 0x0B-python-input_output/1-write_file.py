#!/usr/bin/python3

"""
function that writes a string to a text file (UTF8)
and returns the number of characters written:
"""


def write_file(filename="", text=""):
    """the Write_file function:

    Args:
        filename : to write in.
        text : text to write
    """
    with open(filename, 'w', encoding="utf_8") as myfile:
        return myfile.write(text)
