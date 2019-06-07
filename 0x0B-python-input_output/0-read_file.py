#!/usr/bin/python3
"""mod docstr"""


def read_file(filename=""):
    """fctn docstr"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
