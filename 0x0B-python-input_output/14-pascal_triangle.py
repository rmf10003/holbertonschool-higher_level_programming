#!/usr/bin/python3
"""pascal triangle function"""


def pascal_triangle(n):
    """funct docstr"""
    lis = []
    if n <= 0:
        return lis
    for i in range(n):
        tmp = [
