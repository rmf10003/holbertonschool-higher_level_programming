#!/usr/bin/python3
"""module"""


def matrix_divided(matrix, div):
    """function"""
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix\
        (list of lists) of integers/floats")
    for item in matrix:
        if type(item) is not list:
            raise TypeError("matrix must be a matrix\
            (list of lists) of integers/floats")
        for x in item:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix\
                (list of lists) of integers/floats")
    l = len(matrix[0])
    for item in matrix:
        if len(item) == 0:
            raise TypeError("matrix must be a matrix\
            (list of lists) of integers/floats")
        if len(item) != l:
            raise TypeError("Each row of the matrix\
            must have the same size")
    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in item] for item in matrix]
