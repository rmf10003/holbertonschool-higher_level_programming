#!/usr/bin/python3
"""module"""


def print_square(size):
    """fctn"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for _ in range(size):
            print('#' * size)
