#!/usr/bin/python3
"""module for square class"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """class for Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """init a square instance with specs"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                                self.id, self.x, self.y,
                                                self.width)
    
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update the attributes of a square instance"""
        keys = ('id', 'size', 'x', 'y')
        if len(args) != 0:
            for k, v in zip(keys, args):
                setattr(self, k, v)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
