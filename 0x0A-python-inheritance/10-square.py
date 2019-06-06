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

    def area(self):
        """method docstr"""
        return self.__size * self.__size
