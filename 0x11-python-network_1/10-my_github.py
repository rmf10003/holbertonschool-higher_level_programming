#!/usr/bin/python3
"""take in a string argument and use requests module to query starwars api"""
import requests
import sys

if __name__ == '__main__':
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    j_dict = r.json()
    print(j_dict.get('id'))
