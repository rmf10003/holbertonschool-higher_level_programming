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
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x, end='')
            print('#' * self.width)
     
    def __str__(self):
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id, self.x, self.y,
                                                self.width, self.height)

    def update(self, *args, **kwargs):
        keys = ('id', 'width', 'height', 'x', 'y')
        if len(args) != 0:
            for k, v in zip(args, keys):
                setattr(self, v, k)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    
