#!/usr/bin/python3
"""
A script that fetches https://intranet.hbtn.io/status
with request module
"""
import requests


def getStatus():
    """
    A function that fetches https://intranet.hbtn.io/status
    with the requests module
    """
    res = requests.get('https://intranet.hbtn.io/status')
    text = res.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(res.reason))


if __name__ == '__main__':
    getStatus()
