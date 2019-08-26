#!/usr/bin/python3
"""take in URL, send a request to URL and display value of X-Reqeust-Id var"""
import urllib.request
import urllib.parse
import urllib.error
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: " + str(e.code))
