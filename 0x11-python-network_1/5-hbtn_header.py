#!/usr/bin/python3
"""take in URL, send a request to URL and display value of X-Reqeust-Id var"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('x-Request-Id'))
