#!/usr/bin/python3
"""Class student
"""


class Student:
    """Instance attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method"""
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in self.__dict__:
                if i in attrs:
                    new_dict[i] = self.__dict__[i]
            return new_dict
