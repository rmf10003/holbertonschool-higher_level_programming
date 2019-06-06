#!/usr/bin/python3
"""mod docstr"""
import json


def save_to_json_file(my_obj, filename):
    """fctn docstr"""
    with open(filename, 'wt') as f:
        json.dump(my_obj, f)
