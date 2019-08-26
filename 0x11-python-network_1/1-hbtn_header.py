#!/usr/bin/python3
"""take in URL, send a request to URL and display value of X-Reqeust-Id var"""
import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    html = response.read()
    print(response.headers.get('X-Request-Id'))
