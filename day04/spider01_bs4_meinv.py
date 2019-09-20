#!/usr/bin/python3
# coding: utf-8
import random

import requests
import time
from bs4 import BeautifulSoup, Tag

from libs import ua


def download(url, data=None, callback=None, **kwargs):
    print('starting %s ' % url)
    print(data)
    time.sleep(random.uniform(3, 5))  # 下载频次
    headers = {
        'User-Agent': ua.get()
    }
    # 判断data是否存在
    if not data:
        resp = requests.get(url, headers=headers, timeout=5)
    else:
        headers['Accept'] = 'application/json, text/javascript, */*; q=0.01'
        headers['Cookie'] = 'wp_xh_session_814d1d62fadab3437f112985c6990bab=ac49810f300c96942f1b6156d993ecfe%7C%7C1569120432%7C%7C1569116832%7C%7C7787c34e33fc8ea5755f905d455ead37; UM_distinctid=16d4c90fbc3152-0517f84df54954-38637501-75300-16d4c90fbc4c2; CNZZDATA1276797113=1322642866-1568947632-%7C1568947632'
        headers['Referer'] = 'http://www.meinv.hk/'
        headers['X-Requested-With'] = 'XMLHttpRequest'
        resp = requests.post(url, data=data, headers=headers, timeout=5)

    if resp.status_code == 200:
        content_type = resp.headers['Content-Type']
        if content_type.startswith('text/'):
            html = resp.text
        else:
            resp_json = resp.json()
            html = resp_json.get('postlist')

        if callback:
            callback(html, **kwargs)
        else:
            parse(html)


def parse(html, **kwargs):
    bs = BeautifulSoup(html, 'lxml')

    content_box_list = bs.find_all('div', class_='content-box')  # list[<Tag>, ...]
    for content_box in content_box_list:
        item = {}
        item['name'] = content_box.find('a').attrs.get('title')
        item['info_url'] = content_box.a['href']  # content_box.a.get('href')
        item['cover_url'] = content_box.a.img.attrs.get('src')

        itempipeline(item)


def itempipeline(item):
    print(item)


if __name__ == '__main__':
    download('http://www.meinv.hk/')

    # 加载更多
    more_url = 'http://www.meinv.hk/wp-admin/admin-ajax.php'

    for page in range(2, 13):
        """
        post请求  
        total=39&action=fa_load_postlist&paged=2&home=true&wowDelay=0.3s
        """
        data = {
            'total': 39,
            'action': 'fa_load_postlist',
            'paged': page,
            'home': True,
            'wowDelay': '0.3s'
        }

        download(more_url, data)
