#!/usr/bin/python3
"""
A Python script that searches twitter
"""
import requests
import sys
import base64


def getBearerToken():
    """
    a function that returns the name of a star wars movie
    """

    # url encode input arguments
    _key = requests.utils.quote(sys.argv[1])
    _secret = requests.utils.quote(sys.argv[2])

    # concat encoded _key and _secret
    concat = ":".join([_key, _secret])
    # Base64 encode string
    encoded_token = base64.b64encode(concat.encode('utf-8'))
    encoded_string = str(encoded_token, 'utf-8')
    # encoded_string = str(encoded_token, 'utf-8')
    content_type = 'application/x-www-form-urlencoded;charset=UTF-8'
    _url = 'https://api.twitter.com/oauth2/token'
    _headers = {'Authorization': "Basic {}".format(encoded_string),
                'Content-Type': content_type}
    _data = 'grant_type=client_credentials'
    res = requests.request('POST', _url, headers=_headers, data=_data)
    return(res.json().get('access_token'))


def searchAPI():
    """
    A function that searches the twitter api
    """

    _search = sys.argv[3]
    _token = getBearerToken()
    _url = 'https://api.twitter.com/1.1/search/tweets.json'
    _params = {'q': _search, 'count': '5',}
    _headers = {'Authorization': "Bearer {}".format(_token)}

    res = requests.request('GET', _url, headers=_headers, params=_params)
    parsed = res.json()
    statuses = parsed.get('statuses')
    for _dict in statuses:
        _id = _dict.get('id')
        _text = _dict.get('text')
        _name = _dict.get('user').get('name')
        print("[{}] {} by {}".format(_id, _text, _name))

if __name__ == '__main__':
    searchAPI()
