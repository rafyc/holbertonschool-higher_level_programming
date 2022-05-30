#!/usr/bin/python3
"""Empty class BaseGeometry.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    def __init__(self, size):
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
        self

    def area(self):
        return (self.__size * self.__size)

    def __str__(self):
        return(f"[Square] {self.__size}/{self.__size}")
