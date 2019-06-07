#!/usr/bin/python3
"""student module for class student"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """initialization function for a student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """pub instance method that retreives dict representation"""
        lis = [dict, list, tuple, str, int, float, bool]
        d = {k: v for k, v in self.__dict__.items() if type(v) in lis}
        if type(attrs) is list and all(type(item) is str for item in attrs):
            return {k: v for k, v in d.items() if k in attrs}
        return d
