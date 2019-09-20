#!/usr/bin/python3
# coding: utf-8
import requests
from bs4 import BeautifulSoup, Tag


def download(url, callback=None):
    resp = requests.get(url)
    if resp.status_code == 200:
        resp.encoding = 'gbk'

        if not callback:
            parse(resp.text)
        else:
            callback(resp.text)


def parse(html):
    bs = BeautifulSoup(html, 'lxml')
    li_tags = bs.select('.list_title li')
    for li_tag in li_tags:
        print(li_tag.b.a['href'], li_tag.b.a.text)

        download('http://www.jokeji.cn' + li_tag.b.a['href'], parse_info)


def parse_info(html):
    bs = BeautifulSoup(html, 'lxml')
    a_tag: Tag = bs.select_one('h1 a')

    title = a_tag.next_sibling.next_sibling.next_sibling
    p_tags = bs.select('#text110>p')
    content = [p.text for p in p_tags]

    # for p in p_tags:
    #     content.append(p.get_text())  # p.text

    itempipeline({
        'title': title,
        'content': content
    })


def itempipeline(item):
    print(item)


if __name__ == '__main__':
    download('http://www.jokeji.cn/list.htm')
