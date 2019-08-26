#!/usr/bin/python3
"""A script that fetches the http response header code"""
import requests
import sys


def getStatus():
    """
    A function that fetches the http response header code
    """
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)

if __name__ == '__main__':
    getStatus()
