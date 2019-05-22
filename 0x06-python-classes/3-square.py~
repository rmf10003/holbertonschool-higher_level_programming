#!/usr/bin/python3
class Square(object):
    """Class square with one attribute.

    Args:
        __size (int): size of a square.

    Raises:
        TypeError: if not an int
        ValueError: if negative int
    """
    def __init__(self, size=0):
        """Initialize class with attributes."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
