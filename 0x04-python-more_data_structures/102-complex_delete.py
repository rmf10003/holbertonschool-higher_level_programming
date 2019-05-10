#!/usr/bin/python3
def complex_delete(d, value):
    l = [k for k, v in d.items() if v == value]
    for k in l:
        del d[k]
    return d
