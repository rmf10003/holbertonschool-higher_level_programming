#!/usr/bin/python3
"""student module for class student"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """initialization function for a student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """pub instance method that retreives dict representation"""
        lis = [dict, list, tuple, str, int, float, bool]
        return {k: v for k, v in self.__dict__.items() if type(v) in lis}
