#!/usr/bin/python3
# coding: utf-8

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.132 Safari/537.36'
}

session = requests.session()  # 创建Session对象
resp = session.get('http://119.3.170.97:8080/',
                   auth=('Li', 'Mi'), headers=headers)
print(resp.text)
print(resp.headers)
print(resp.cookies)

resp = session.get('http://119.3.170.97:8080/hi.html',
                   auth=('Li', 'Mi'),
                   headers=headers)
print(resp.text)
print(resp.request.headers)
