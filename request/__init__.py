#!/usr/bin/python3
# coding: utf-8
from http.client import HTTPResponse
from urllib.request import Request, urlopen, urlretrieve
from urllib.parse import urlencode

"""
get('http://www.baidu.com/s?', {'limit': 20})
"""

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def get(url,
        params: dict = None,
        headers: dict = None) -> HTTPResponse:
    """

    :param url:
    :param params:
    :param headers:
    :return:
    """

    if params:
        params_str = urlencode(params)

        suffix = '?' if url.find('?') == -1 else '' if url.find('=') == -1 else '&'
        url += suffix+params_str
    if headers:
        req = Request(url, headers=headers)
    else:
        req = Request(url)

    return urlopen(req)


def save_file(url, filename):
    urlretrieve(url, filename)
