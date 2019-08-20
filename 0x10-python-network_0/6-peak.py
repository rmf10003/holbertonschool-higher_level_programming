#!/usr/bin/python3
"""find peak of int array"""


def find_peak(lis):
    """find the peak integer"""
    for i in range(len(lis)):
        if i + 1 >= len(lis):
            return lis[i]
        elif lis[i] > lis[i + 1]:
            return lis[i]
