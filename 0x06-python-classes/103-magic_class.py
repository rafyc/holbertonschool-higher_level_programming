#!/usr/bin/python3
"""
Class Square defines a square
"""
import dis
import math


class MagiClass:

    def __init__(self, radius=0):
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        return (2 * math.pi) * self.__radius


dis.dis(MagiClass)
