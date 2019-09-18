#!/usr/bin/python3
# coding: utf-8
import hashlib

from lxml import etree

from request import get, save_file

url = 'http://sc.chinaz.com/tupian/shuaigetupian.html'


def download(url, callback):
    resp = get(url)
    if resp.code == 200:
        html = resp.read().decode('utf-8')
        # print(html)
        callback(html)


def parse(html):
    root = etree.HTML(html)
    imgs_elements = root.xpath('//div[starts-with(@class, "box")]/div/a')
    for img_a_element in imgs_elements:
        # img_a_element -> Element(.text,  .get(),  .xpath())
        info_url = img_a_element.get('href')
        name = img_a_element.get('alt')

        cover_url = img_a_element.xpath('./img/@src2')[0]

        print(name, info_url, cover_url)
        save(cover_url, True)


def save(url, flag=False):
    filename = url.split('/')[-1]
    if flag:
        ext = filename.split('.')[-1]
        filename = hashlib.md5(url.encode('utf-8')).hexdigest()+"."+ext

    print(filename)
    save_file(url, 'images/' + filename)


if __name__ == '__main__':
    download(url, parse)
