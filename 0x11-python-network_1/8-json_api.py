#!/usr/bin/python3
"""take in URL, send a request to URL and display value of X-Reqeust-Id var"""
import requests
import sys

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    payload = {'q': ""}
    if len(sys.argv) > 1:
        payload['q'] = sys.argv[1]
    r = requests.post(url, data=payload)
    try:
        j_dict = r.json()
        if not j_dict:
            print('No result')
        else:
            id = j_dict.get('id')
            name = j_dict.get('name')
            print("[{}] {}".format(id, name))
    except ValueError as e:
        print("Not a valid JSON")
