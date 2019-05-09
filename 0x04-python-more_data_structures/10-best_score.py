#!/usr/bin/python3
def best_score(d):
    if d == {} or d is None:
        return None
    return max(d.items(), key=lambda t: t[1])[0]
