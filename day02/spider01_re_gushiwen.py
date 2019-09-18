#!/usr/bin/python3
# coding: utf-8
import re
from urllib.request import urlopen, Request, build_opener, ProxyHandler, HTTPHandler

import ssl

import time

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.gushiwen.org'


opener = build_opener(HTTPHandler(), ProxyHandler({
    'http': 'http://219.159.38.208:56210'
}))

def download(url):
    request = Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.132 Safari/537.36'
    })
    resp = opener.open(request)
    if resp.code == 200:
        bytes = resp.read()
        html = bytes.decode('utf-8')
        parse(html)


def parse(html):
    titles = re.findall('<b>(.*?)</b>', html)
    authors = re.findall('<p class="source">.*?<a .*?>(.*?)</a>.*?<a .*?>(.*?)</a>', html)

    # re.DOTALL 表示.包含任意字符和换行符
    contents = re.findall(r'<div class="contson" .*?>(.*?)</div>', html, re.DOTALL)

    print(list(zip(titles, authors)))
    print(contents)

    # 数据存储（mysql/oracle, es搜索）

    # 提取下一页url
    next_url = re.findall('<a id="amore" .*?href="(.*?)"', html)

    if titles:
        next_url = 'https://www.gushiwen.org'+next_url[0]
        print(next_url)

        time.sleep(.5)
        download(next_url)

    print('完成任务')

if __name__ == '__main__':
    download(url)
