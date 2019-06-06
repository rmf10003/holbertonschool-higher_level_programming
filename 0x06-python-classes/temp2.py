#!/usr/bin/python3
class Square:
    def __init__(self, another=0):
        self.other = another


    def area(self):
        return self.__size ** 2

    @property
    def other(self):
        return self.__size

    @size.setter
    def other(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if self.other == 0:
            print()
        for i in range(self.other):
            print("#" * self.other)
