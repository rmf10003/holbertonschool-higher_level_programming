#!/usr/bin/python3
class Square(object):
    """Class square with one attribute.

    Args:
        __size (int): size of a square.
        __position (tuple): tuple of two positive int coordinates

    Raises:
        TypeError: if not an int
        ValueError: if negative int
        TypeError: if not tup of 2 positive ints
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize class with attributes."""
        self.__size = size
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(x, int) for x in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif all(x < 0 for x in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """Gets the value of __size

        Sets the value of __size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """get and set falue of property"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not all(isinstance(x, int) for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif all(x < 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """squares the size of the square.

        Returns:
            the current square area.
        """
        return self.__size ** 2

    def my_print(self):
        """prints square with '#' char to stdout"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end='')
                for j in range(0, self.__size):
                    print("#", end="")
                print()
