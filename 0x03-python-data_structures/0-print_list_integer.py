#!/usr/bin/python3
"""print list integer"""
def print_list_integer(my_list=[]):
    """print a list of integers to the standard out"""
    for num in my_list:
        print("{:d}".format(num))
