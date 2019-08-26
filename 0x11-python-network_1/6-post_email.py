#!/usr/bin/python3
"""A script sends an email"""
import requests
import sys


def sendEmail():
    """
    A function that sends POST and prints the response
    """
    _data = {'email': sys.argv[2]}
    _url = sys.argv[1]
    res = requests.request('POST', _url, data=_data)
    print(res.text)

if __name__ == '__main__':
    sendEmail()
