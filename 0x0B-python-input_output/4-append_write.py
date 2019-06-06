#!/usr/bin/python3
"""module docstr"""


def append_write(filename="", text=""):
    """fctn docstr"""
    with open(filename, 'at') as f:
        return f.write(text)
