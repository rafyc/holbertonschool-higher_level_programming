#!/usr/bin/python3
"""the say_my_name function."""


def say_my_name(first_name, last_name=""):
    """function that print the full name

    Args:
        first_name (str): the frist name
        last_name (str, optional): the last name. Defaults to "".
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
