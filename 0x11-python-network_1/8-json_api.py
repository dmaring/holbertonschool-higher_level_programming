#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_userA
script sends an email
"""
import requests
import sys


def searchAPI():
    """
    A function that sends POST and prints the response
    """
    if len(sys.argv) < 2:
        _data = {'q': ""}
    else:
        _data = {'q': sys.argv[1]}
    _url = 'http://172.31.54.208:47065/search_user'
    res = requests.request('POST', _url, data=_data)
    try:
        _json = res.json()
        if not _json:
            print("No result")
        else:
            print("[{}] {}".format(_json.get('id'), _json.get('name')))
    except:
        print("Not a valid JSON")


if __name__ == '__main__':
    searchAPI()
