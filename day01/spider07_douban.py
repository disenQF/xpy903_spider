#!/usr/bin/python3
# coding: utf-8
from urllib.request import urlopen, Request
from urllib.parse import urlencode

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import time

url = 'https://movie.douban.com/j/chart/top_list'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.132 Safari/537.36'
}

def download(page):
    params = {
        'type': 5,
        'interval_id': '80:70',# 100:90, 90:80, 80:70
        'start': (page-1)*20,
        'limit': 20
    }

    request = Request(url+"?"+urlencode(params),
                      headers=headers)

    resp = urlopen(request)

    if resp.code == 200:
        with open('json_/douban_%s.json' % page, 'wb') as f:
            f.write(resp.read())


if __name__ == '__main__':
    for page in range(1, 6):
        download(page)




