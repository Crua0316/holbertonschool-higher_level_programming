#!/usr/bin/python3
"""
Function that writes a string to a text (utf-8) & return N char
"""


def write_file(filename="", text=""):
    """
    Args:
        Filename (str): [file to open and read or create].
        Text (str): [text to write].
    Return:
        [int]: [number of characters]
    """
    lines = 0
    with open(filename, 'w') as f:
        lines = f.write(text)
    return lines
