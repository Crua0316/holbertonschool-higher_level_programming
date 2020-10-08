#!/usr/bin/python3
"""
Function that returns the JSON repres object(str)
"""


import json


def to_json_string(my_obj):
    """Use json.dumps"""
    data_read = json.dumps(my_obj)
    return data_read
