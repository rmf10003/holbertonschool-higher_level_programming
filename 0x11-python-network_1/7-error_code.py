#!/usr/bin/python3
"""use requests module to fetch a page given a url and handle error code"""
import requests
import sys

if __name__ is '__main__':
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: " + str(r.status_code))
    else:
        print(r.text)
