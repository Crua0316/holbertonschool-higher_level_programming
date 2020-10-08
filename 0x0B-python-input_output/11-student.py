#!/usr/bin/python3
"""Class student
"""


class Student:
    """Instance attributes"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """Public method"""
    def to_json(self):
        return vars(self)
