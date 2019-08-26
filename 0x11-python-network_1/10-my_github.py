#!/usr/bin/python3
"""
A Python script that uses the Github API to return the userid
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


def searchAPI():
    """
    A function that uses the Github API to return the userid
    """
    res = requests.get('http://api.github.com/user',
                       auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    _dict = res.json()
    print(_dict.get('id'))


if __name__ == '__main__':
    searchAPI()
