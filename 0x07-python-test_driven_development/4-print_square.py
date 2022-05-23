#!/usr/bin/python3
"""The print_square function"""


def print_square(size):
    """The function that print a square

    Args:
        size(int): the square size
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print("#" * size, end="")
            print()
