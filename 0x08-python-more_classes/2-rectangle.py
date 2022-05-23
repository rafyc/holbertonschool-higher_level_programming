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
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif type(height) is not int:
            raise ValueError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("width must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        @property method retrieve the data.
        Return the width of a rectangle
        """
        return self.___width

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
        elif type(value) is not int:
            raise ValueError("width must be an integer")
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
        elif type(value) is not int:
            raise ValueError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """
        The area method is a public instance.
        Return the current Rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        The perimeter method is a public instance.
        Return the current Rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return
        return (self.__height + self.__width) * 2
