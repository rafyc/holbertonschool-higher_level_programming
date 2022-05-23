#!/usr/bin/python3
"""
Class Rectangle defines a Rectangle
"""


class Rectangle:
    """
    Class that defines a Rectangle
    """

    def __init__(self, width=0, height=0):
        """ __init__ method to create an object instance of the class

        Args:
            width: size of the rectangle. Defaults to 0.
            height: height of the rectangle. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        @property method retrieve the data.
        Return the width of a rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        @property method retrieve the data.
        Return the height of a rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        @width.setter method change the data.
        Args:
        - value (int): the width of the rectangle, must be an integer
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """
        @height.setter method change the data.
        Args:
        - value (int): the height of the rectangle, must be an integer
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
