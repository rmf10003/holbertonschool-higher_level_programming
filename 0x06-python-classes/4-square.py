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
        self.__size = size

    @property
    def size(self):
        """Gets the value of __size

        Sets the value of __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """squares the size of the square.

        Returns:
            the current square area.
        """
        return self.__size ** 2
