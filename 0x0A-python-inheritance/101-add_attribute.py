#!/usr/bin/python3
"""Def attribute function"""


def add_attribute(obj, key, value):
    """Adds a new attribute to an object if it’s possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
