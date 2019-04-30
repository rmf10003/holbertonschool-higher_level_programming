#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        char = str[c]
        if ord('z') >= ord(char) >= ord('a'):
            char = chr(ord(char) - 32)
        if c == len(str) - 1:
            print("{}".format(char))
        else:
            print("{}".format(char), end='')
