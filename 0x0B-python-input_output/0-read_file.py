#!/usr/bin/python3
"""Read_file function"""


def read_file(filename=""):
    """Print
    Args:
        Filename (str, ""): [name file passed to read].
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
