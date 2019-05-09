#!/usr/bin/python3
def simple_delete(d, key=""):
    if key in d:
        del d[key]
    return d
