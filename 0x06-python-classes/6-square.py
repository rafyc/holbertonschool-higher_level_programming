#!/usr/bin/python3
"""Class Square defines a square:
- Size : Private instance attribute
- Instantiation with size (no type/value verification)
"""


class Square:
    """
    The class Square define a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        The __init__ method is used. This method run as soon as an object of
        a classe is instantiated (= created).

        Args:
            size (int): the size of the square, must be an integer

        Attribute:
        - __size: the size is a private attribute (that means the acces to
        variable size is restricted)

        Raises:
            TypeError: is not a int
            ValueError: is negative
        """
        self.__size = size
        self.__position = position

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

    @property
    def size(self):
        """
        @property method retrieve the data.
        Return the size of a square
        """
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        """
        @size.setter method change the data.
        Args:
        - value (int): the size of the square, must be an integer
        """
        self.__size = value

        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @position.setter
    def position(self, value):
        """
        @position.setter method change the square's position
        Args:
        - value (tuple): the position of the square, must be a tuple
          and 2 positive integers
        """
        self.__position = value
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """
        The area method is a public instance.
        Return the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        The my_print method prints in stdout
        the square with '#'
        """
        if self.__size == 0:
            print("")

        elif self.position[1] > 0:
            for pos1 in range(self.__position[1]):
                print("")

        for line in range(self.__size):
            for pos0 in range(self.__position[0]):
                print(" ", end="")
            for column in range(self.__size):
                print("#", end="")
            print("")
