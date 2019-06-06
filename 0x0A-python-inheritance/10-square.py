#!/usr/bin/python3
"""mod docstr"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """class docstr"""

    def __init__(self, size):
        """method docstr"""
        super().super().integer_validator(size)
        self.__size = size

    def area(self):
        """method docstr"""
        self.__size
