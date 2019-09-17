#!/usr/bin/python3
# coding: utf-8

from urllib.request import urlopen
from urllib.parse import quote, unquote, urlencode
from urllib.request import Request


import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.baidu.com/s?wd='+quote('香港', encoding='utf-8')  # url路径中存在中文时，需要编码

# 通过Request对象封装请求及请求头的相关信息
# 如果data包含的指定的内容，则表示请求方法是POST, data是字节类型
req = Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.132 Safari/537.36'
})

resp = urlopen(req)  # urlopen()可以直接请求URL，也可以请求Request对象。
print(resp.code)
bytes = resp.read()
print(bytes.decode('utf-8'))