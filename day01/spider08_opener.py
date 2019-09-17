#!/usr/bin/python3
# coding: utf-8
import json
from urllib.request import HTTPHandler, HTTPCookieProcessor, ProxyHandler
from http.cookiejar import CookieJar
from urllib.request import build_opener
from urllib.request import Request
from urllib.parse import urlencode

import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def get_jd():
    url = 'http://jd.com'
    request = Request(url)

    # 生成opener对象（浏览器）
    httphandler = HTTPHandler()
    opener = build_opener(httphandler)  # 可以增加多个处理器Handler

    # 通过opener发起请求
    resp = opener.open(request)
    if resp.code == 200:
        bytes = resp.read()
        print(bytes.decode('utf-8'))


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/76.0.3809.132 Safari/537.36',
    'X-Requested-with': 'XMLHttpRequest',
    'Referer': 'http://www.renren.com/'
}

# 构建opener, 支持HTTP请求和Cookie的处理
opener = build_opener(HTTPHandler(),
                      HTTPCookieProcessor(CookieJar()))


def login():
    url = 'http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2019821521164'
    data = {
        'email': '610039018@qq.com',
        'origURL': 'http://www.renren.com/home',
        'domain': 'renren.com',
        'key_id': 1,
        'captcha': 'web_login',
        'password': '3fa5ee1cc182f47fe3103b6170aeeb2d3bd291e15a479a2700346e9cff084968',
        'rkey': '4dbb3a17871b6815976ebba83bb808c2'
    }
    req = Request(url, urlencode(data).encode('utf-8'), headers)
    resp = opener.open(req)
    if resp.code == 200:
        bytes = resp.read()
        resp_json = json.loads(bytes.decode('utf-8'))
        if resp_json.get('code'):
            get_profile()
        else:
            print(resp_json)


def get_profile():
    url = 'http://www.renren.com/958915617'
    print('开始获取用户的信息')
    resp = opener.open(url)
    if resp.code == 200:
        bytes = resp.read()
        print(bytes.decode('utf-8'))


def proxy_get(url):
    opener = build_opener(HTTPHandler(),
                         HTTPCookieProcessor(CookieJar()),
                         ProxyHandler(proxies={'https': '113.119.38.80:3128'}))
    resp = opener.open(url, timeout=10)
    if resp.code == 200:
        bytes = resp.read()
        # print(bytes.decode('utf-8'))
        with open('baidu_ip.html', 'wb') as f:
            f.write(bytes)


if __name__ == '__main__':
    proxy_get('http://www.baidu.com/s?wd=ip')
