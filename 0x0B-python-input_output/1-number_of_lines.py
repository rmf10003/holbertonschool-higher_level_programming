#!/usr/bin/python3
"""mod docstr"""


def number_of_lines(filename=""):
    """fctn docstr"""
    i = 0
    with open(filename, 'r') as f:
        for line in f:
            i += 1
        return i
