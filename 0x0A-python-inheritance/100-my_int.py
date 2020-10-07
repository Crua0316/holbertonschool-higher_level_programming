#!/usr/bin/python3
"""Module comparitions"""


class MyInt(int):
    """Swapped == and =!"""
    def __eq__(self, value):
        """Return opposite"""
        return (int(self) != int(value))

    def __ne__(self, value):
        """Return opposite"""
        return(int(self) == int(value))
