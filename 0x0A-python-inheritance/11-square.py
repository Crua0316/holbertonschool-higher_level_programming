#!/usr/bin/python3
"""
Basegeometry method
"""


class BaseGeometry:
    """Area with raise Exception"""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")
    """Integer_validator"""

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle representation"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """String of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """Represent square"""
    def __init__(self, size):
        """Init with super function to use all attributes from parent class
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"Square area"""
        return self.__size ** 2

    def __str__(self):
        """String of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
