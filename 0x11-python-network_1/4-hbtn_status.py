#!/usr/bin/python3
"""
A script that fetches https://intranet.hbtn.io/status
with request module
"""
import requests
import sys


def getStatus():
    """
    A function that fetches https://intranet.hbtn.io/status
    with the requests module
    """
    res = requests.get('https://intranet.hbtn.io/status')
    print(res.status_code)


if __name__ == '__main__':
    getStatus()
