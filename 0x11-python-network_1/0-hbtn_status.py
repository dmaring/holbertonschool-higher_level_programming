#!/usr/bin/python3
"""A script that fetches https://intranet.hbtn.io/status"""
import urllib.request


def getStatus():
    """
    A function that fetches https://intranet.hbtn.io/status
    """
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        content = res.read()
        c_type = type(content.decode())
        headers = res.headers
        print("Body response:")
        print("\t- type: {}".format(c_type))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8'))

if __name__ == '__main__':
    getStatus()
