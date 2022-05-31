#!/usr/bin/python3

"""
function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """The read_file function

    Args:
        filename : the file to open.
    """
    with open(filename, 'r', encoding="utf-8") as myfile:
        print(f"{myfile.read()}", end="")
