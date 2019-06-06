#!/usr/bin/python3
"""mod docstr"""


class BaseGeometry:
    """class docstr"""

    def area(self):
        """method docstr"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """method docstr"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value < 1:
            raise ValueError('{} must be greater than 0'.format(name))
