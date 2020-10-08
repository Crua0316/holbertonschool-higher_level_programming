#!/usr/bin/python3
"""
Function that writes an object to text
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        My_obj: [objecto to writes]
        Filename: [text file]
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
