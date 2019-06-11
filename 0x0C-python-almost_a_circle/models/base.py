#!/usr/bin/python3
"""module for Base class"""


class Base:
    """Base is the base class of all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """method for initializing instances of Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
