#!/usr/bin/python3
"""mod docstr"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """class docstr"""

    def __init__(self, size):
        """method docstr"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """method docstr"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """method docstr"""
        return self.__size * self.__size
