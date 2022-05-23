#!/usr/bin/python3
"""the say_my_name function."""


def say_my_name(first_name, last_name=""):
    """function that print the full name

    Args:
        first_name (str): the frist name
        last_name (str, optional): the last name. Defaults to "".
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    elif isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
