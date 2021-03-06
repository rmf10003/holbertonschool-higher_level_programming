#!/usr/bin/python3
"""mod docstr"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class str"""

    def __init__(self, width, height):
        """method docstr"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """method docstr"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """fctn docstring"""
        return self.__width * self.__height
