#!/usr/bin/python3
"""The rectangle class
    """

from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ __init__ method to create an object instance of the class Base

        Args:
            width (_type_): width of the rectangle
            height (_type_): height of the rectangle
            x (int): _description_. Defaults to 0.
            y (int): _description_. Defaults to 0.
            id (_type_): id of the object. Defaults to None.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

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

    @property
    def x(self):
        """
        @property method retrieve the data.
        Return the x
        """
        return self.__x

    @property
    def y(self):
        """
        @property method retrieve the data.
        Return the y
        """
        return self.__y

    @width.setter
    def width(self, val):
        """

        @width.setter method change the data.
        Args:
        - val (int): the width of the rectangle, must be an integer
        """
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @height.setter
    def height(self, val):
        """

        @height.setter method change the data.
        Args:
        - val (int): the height of the rectangle, must be an integer
        """
        if type(val) is not int:
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @ x.setter
    def x(self, val):
        """
        @x.setter method change the data.
        Args:
        - val (int): the x of the rectangle, must be an integer
        """
        if type(val) is not int:
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")

        self.__x = val

    @ y.setter
    def y(self, val):
        """
        @y.setter method change the data.
        Args:
        - val (int): the y of the rectangle, must be an integer
        """
        if type(val) is not int:
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """
        The area method is a public instance.
        Return the current Rectangle area
        """
        return self.__width * self.__height

    def display(self):
        """methond that display the rectangle
        """

        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        The instance method that returns an 'informal' and nicely printable
        string representation of an instance.
        """
        id = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return f"[Rectangle] ({id}) {x}/{y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """function that assigns an argument to each attribute"""
        if len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "y" in kwargs:
                self.y = kwargs["y"]
            if "x" in kwargs:
                self.x = kwargs["x"]

    def to_dictionary(self):
        """public method def to_dictionary(self): that returns
        the dictionary representation of a Rectangle:
        """
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y,
        }
