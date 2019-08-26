#!/usr/bin/python3
"""
A Python script that uses the Github API to return the information
"""
import requests
import sys
from requests.auth import HTTPBasicAuth


def searchAPI():
    """
    A function that uses the Github API to return the userid
    """
    user = sys.argv[1]
    repo = sys.argv[2]
    res = requests.get('http://api.github.com/repos/{}/{}/commits'
                       .format(repo, user))
    _list = res.json()
    _len = len(_list)
    if _len > 10:
        _len = 10
    for i in range(_len):
        _sha = _list[i].get('sha')
        name = _list[i].get('commit').get('author').get('name')
        print("{}: {}".format(_sha, name))

if __name__ == '__main__':
    searchAPI()
