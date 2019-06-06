#!/usr/bin/python3
"""mod docstr"""
import json


def load_from_json_file(filename):
    """fctn docstr"""
    with open(filename, 'rt') as f:
        return json.load(f)
