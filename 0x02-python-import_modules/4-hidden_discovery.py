#!/usr/bin/python3
import inspect
import hidden_4
if __name__ == '__main__':
    func = inspect.getmembers(hidden_4, inspect.isfunction)
    for i in func:
        print(i[0])
