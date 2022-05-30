#!/usr/bin/python3
"""Create a class MyInt that inherits from int
"""


class MyInt(int):
    """
    The class MyInt that inherits from int:
    """

    def __init__(self, b):
        """The initialize method"""
        self.__b = b

    def __eq__(self, b):
        """The equal method return non-equal value"""
        return self.__b != self.__b

    def __ne__(self, b):
        """The non-equal method return equal value"""
        return self.__b == self.__b
