#!/usr/bin/python3

class MyInt(int):

    def __init__(self, b):
        self.__b = b

    def __eq__(self, b):
        return self.__b != self.__b

    def __ne__(self, b):
        return self.__b == self.__b
