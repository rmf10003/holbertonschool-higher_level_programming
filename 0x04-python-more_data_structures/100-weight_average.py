#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    numer, denom = 0, 0
    for tup in my_list:
        numer += tup[0] * tup[1]
        denom += tup[1]
    return numer / denom
