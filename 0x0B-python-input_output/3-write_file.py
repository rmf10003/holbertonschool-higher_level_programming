#!/usr/bin/python3
"""module docstr"""


def write_file(filename="", text=""):
    """fctn docstr"""
    with open(filename, 'wt') as f:
        return f.write(text)
