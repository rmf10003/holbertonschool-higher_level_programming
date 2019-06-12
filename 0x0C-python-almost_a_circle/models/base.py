#!/usr/bin/python3
"""module for Base class"""
import json
import io


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of lists of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries, skipkeys=True)

    @classmethod
    def save_to_file(cls, list_objs):
        """write JSON string repr of a list of all instances to a file"""
        with open("{}.json".format(cls.__name__), 'wt') as file:
            if list_objs is None:
                file.write('[]')
            else:
                l = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(l))
                    
