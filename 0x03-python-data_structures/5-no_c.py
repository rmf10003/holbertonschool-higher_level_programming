#!/usr/bin/python3
def no_c(my_string):
    L2 = [char for char in my_string if char not in 'Cc']
    return ''.join(L2)
