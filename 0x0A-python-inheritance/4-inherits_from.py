#!/usr/bin/python3
"""mod docstr"""


def inherits_from(obj, a_class):
    """def docstr"""
    if isinstance(obj, a_class):
        if type(obj) != a_class:
            return True
    return False
