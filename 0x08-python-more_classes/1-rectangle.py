#!/usr/bin/python3
"""Class to Rectangle
"""


class Rectangle:
    """Creates base height and width of the rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization of rectangle
        Args:
            width: size of width.
            height: size of height.
        Attributes:
            width: width of the rectangle.
            height: heigth of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """property of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        Args:
            Value: size of width.
        Raises:
            TypeError: when value is not an int.
            ValueError: value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """property of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        Args:
            Value: size of height.
        Raises:
            TypeError: When value is not an int.
            ValueError: Value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
