#!/usr/bin/python3
def roman_to_int(rs):
    if type(rs) is not str or rs is None:
        return 0
    conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ival = 0
    for l in range(len(rs)):
        if l == 0 or conv[rs[l]] <= conv[rs[l]]:
            ival += conv[rs[l]]
        else:
            ival += conv[rs[l]] - 2 * conv[rs[l - 1]]
    return ival
