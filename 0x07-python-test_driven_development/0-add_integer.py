#!/usr/bin/python3
"""
the add_integer function
"""


def add_integer(a, b=98):
    """Fonction that add 2 integers

    Args:
        a (int): _description_
        b (int, optional): Defaults to 98.

    Returns:
        int: a + b
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
