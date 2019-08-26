#!/usr/bin/python3
"""A script that fetches https://intranet.hbtn.io/status"""
import urllib.request
import sys


def getStatus():
    """
    A function that fetches https://intranet.hbtn.io/status
    """
    with urllib.request.urlopen(sys.argv[1]) as res:
        content = res.read()
        c_type = type(content)
        headers = res.headers
        print(headers['X-Request-Id'])


if __name__ == '__main__':
    getStatus()
