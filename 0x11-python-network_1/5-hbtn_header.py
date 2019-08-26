#!/usr/bin/python3
"""
A script that fetches a header value for X-Request-Id
"""
import requests
import sys


def getStatus():
    """
    A function that fetches a header value for X-Request-Id
    """
    res = requests.get(sys.argv[1])
    _id = res.headers.get('X-Request-Id')
    print(_id)


if __name__ == '__main__':
    getStatus()
