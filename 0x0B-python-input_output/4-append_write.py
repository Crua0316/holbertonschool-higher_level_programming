#!/usr/bin/python3
"""
Funct that appends a string at the end of a text file & return # char
"""


def append_write(filename="", text=""):
    """
    Args:
        Filename (str): [file to open and read or create].
        Text (str): [text to write].
    Return:
        [int]: [number of characters]
    """
    with open(filename, 'a') as f:
        read_data = f.write(text)
    return read_data
