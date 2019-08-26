#!/usr/bin/python3
"""A script that fetches https://intranet.hbtn.io/status"""
import urllib.request
import urllib.error
import sys


def getStatus():
    """
    A function that fetches https://intranet.hbtn.io/status
    """
    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            content = res.read()
            print(content.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == '__main__':
    getStatus()
