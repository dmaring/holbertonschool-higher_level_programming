#!/usr/bin/python3
"""
A Python script that searches the star wars api
"""
import requests
import sys


def movieName(url, session):
    """
    a function that returns the name of a star wars movie
    """

    res = session.get(url)
    title = res.json().get('title')
    return(title)


def searchAPI():
    """
    A function that searches the star wars api
    """
    _params = {'search': sys.argv[1]}
    _url = 'https://swapi.co/api/people/'
    s = requests.Session()
    res = s.request('GET', _url, params=_params)
    _dict = res.json()
    print("Number of results: {}".format(_dict.get('count')))
    for result in _dict.get('results'):
        print(result.get('name'))
        for film in result.get('films'):
            print("\t{}".format(movieName(film, s)))
    while _dict.get('next'):
        _url = _dict['next']
        res = s.request('GET', _url)
        _dict = res.json()
        for result in _dict.get('results'):
            print(result.get('name'))
            for film in result.get('films'):
                print("\t{}".format(movieName(film, s)))


if __name__ == '__main__':
    searchAPI()
