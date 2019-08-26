#!/usr/bin/python3
"""take in a string argument and use requests module to query starwars api"""
import requests
import sys

if __name__ == '__main__':
    url = "https://swapi.co/api/people"
    search = sys.argv[1]
    r = requests.get(url, params={'search': search})
    j_dict = r.json()
    print("Number of results: {}".format(j_dict.get('count')))
    for character in j_dict.get('results'):
        print(character.get('name'))
