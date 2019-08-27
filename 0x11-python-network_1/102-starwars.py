#!/usr/bin/python3
"""
A Python script that searches the star wars api
"""
import requests
import sys


def movieName(url):
    """
    a function that returns the name of a star wars movie
    """

    res = requests.get(url)
    title = res.json().get('title')
    return('\t{}'.format(title))


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
        for film in result.get('films'):
            print(movieName(film))
    while _dict.get('next'):
        _url = _dict['next']
        res = requests.request('GET', _url)
        _dict = res.json()
        for result in _dict.get('results'):
            print(result.get('name'))
            for film in result.get('films'):
                print(movieName(film))


if __name__ == '__main__':
    searchAPI()
