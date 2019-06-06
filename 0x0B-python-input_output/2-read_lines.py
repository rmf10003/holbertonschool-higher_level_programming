#!/usr/bin/python3
"""mod docstr"""


def read_lines(filename="", nb_lines=0):
    """fctn docstr"""
    i = 0
    with open(filename, 'r') as f:
        for line in f:
            i += 1
        f.seek(0)
        if nb_lines <= 0 or nb_lines >= i:
            print(f.read(), end='')
        else:
            for _ in range(nb_lines):
                print(f.readline(), end='')
