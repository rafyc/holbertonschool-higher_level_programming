#!/usr/bin/python3
"""Empty class BaseGeometry.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    The class Square define:
        * Instantiation with size: def __init__(self, size)
        * the area() method must be implemented
    """

    def __init__(self, size):
        """
        The initialization method of class Square.
        Args:
            - __size (int, private)
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size
        self

    def area(self):
        """
        The method that compute the area of a square.
        """
        return (self.__size * self.__size)

    def __str__(self):
        """
        The method that print the area of a square.
        """
        return(f"[Square] {self.__size}/{self.__size}")
