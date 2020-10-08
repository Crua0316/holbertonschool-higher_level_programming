#!/usr/bin/python3
"""
Function that return the number of lines
"""


def number_of_lines(filename=""):
    """
    Args:
        Filename (str, ""): [text file to open and read].
        Returns: [int]: [numb lines]
    """
    lines_numb = 0
    with open(filename, 'r') as f:
        for i in f:
            lines_numb += 1
    return lines_numb
