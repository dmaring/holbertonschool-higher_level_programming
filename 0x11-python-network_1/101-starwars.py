#!/usr/bin/python3
"""
A Python script that searches the star wars api
"""
import requests
import sys


def searchAPI():
    """
    A function that searches the star wars api
    """
    _params = {'search': sys.argv[1]}
    _url = 'https://swapi.co/api/people/'
    res = requests.request('GET', _url, params=_params)
    _dict = res.json()
    print("Number of results: {}".format(_dict.get('count')))
    for result in _dict.get('results'):
        print(result.get('name'))
    while _dict.get('next'):
        _url = _dict['next']
        res = requests.request('GET', _url)
        _dict = res.json()
        for result in _dict.get('results'):
            print(result.get('name'))


if __name__ == '__main__':
    searchAPI()
