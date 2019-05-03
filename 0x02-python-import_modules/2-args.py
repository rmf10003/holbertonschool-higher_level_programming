#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    if len(argv - 1) == 1:
        print("{} argument:".format(len(argv) - 1))
    else
        print("{} arguments:".format(len(argv) - 1), end="")
        if len(argv - 1) == 0:
            print(".")
        else:
            print(":")
    for i in range(len(argv - 1)):
            
