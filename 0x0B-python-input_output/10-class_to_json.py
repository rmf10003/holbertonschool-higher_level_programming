#!/usr/bin/python3
"""module for class_to_json"""


def class_to_json(obj):
    """function that returns the dictionary description with simple data"""
    lis = [dict, list, tuple, str, int, float, bool]
    return {k: v for k, v in obj.__dict__.items() if type(v) in lis}
