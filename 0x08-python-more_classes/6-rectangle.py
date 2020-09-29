#!/usr/bin/python3
"""Class to Rectangle
"""


class Rectangle:
    """Creates base height and width of the rectangle"""

    number_of_instances = 0

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
        Rectangle.number_of_instances += 1

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
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
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
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

    def area(self):
        """Gets the ares of the Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Gets the perimeter of the rectangle"""
        if (self.width or self.height) == 0:
            return 0
        return(2 * self.height) + (2 * self.width)

    def __str__(self):
        """Return string of rectangles with #"""
        if (self.width or self.height) == 0:
            return ""
        rec = "#" * self.width
        return "\n".join(list(rec for a in range(self.height)))

    def __repr__(self):
        """Return string representation of Rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Delete the square input"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
