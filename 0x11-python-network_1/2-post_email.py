#!/usr/bin/python3
"""A script sends an email"""
import urllib.request
import urllib.parse
import sys


def sendEmail():
    """
    A function that sends POST and prints the response
    """
    values = {'email': sys.argv[2]}
    url = sys.argv[1]
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        content = res.read()
        print(content.decode('utf-8'))

if __name__ == '__main__':
    sendEmail()
