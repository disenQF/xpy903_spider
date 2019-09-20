#!/usr/bin/python3
# coding: utf-8

import requests
from bs4 import BeautifulSoup, Tag

from libs import ua


def download(url, data=None, callback=None, **kwargs):
    headers = {
        'User-Agent': ua.get()
    }
    # 判断data是否存在
    if not data:
        resp = requests.get(url, headers=headers)
    else:
        resp = requests.post(url, data=data, headers=headers)

    if resp.status_code == 200:
        if callback:
            callback(resp.text, **kwargs)
        else:
            parse(resp.text)


def parse(html, **kwargs):
    bs = BeautifulSoup(html, 'lxml')

    tag: Tag = bs.find('title')  # bs4.element.Tag
    print(type(tag), tag, tag.text, sep='\n')

    content_box_list = bs.find_all('div', class_='content-box')  # list[<Tag>, ...]
    for content_box in content_box_list:
        print(content_box.find('a').attrs.get('title'))
        print(content_box.a.img.attrs.get('src'))

    # 加载更多
    more_url = 'http://www.meinv.hk/wp-admin/admin-ajax.php'
    """
    post请求  
    total=39&action=fa_load_postlist&paged=2&home=true&wowDelay=0.3s
    """
    data = {
        'total': 39,
        'action': 'fa_load_postlist',
        'paged': 2,
        'home': True,
        'wowDelay': '0.3s'
    }
    pass


def itempipeline(item):
    pass


if __name__ == '__main__':
    download('http://www.meinv.hk/')
