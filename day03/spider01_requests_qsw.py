#!/usr/bin/python3
# coding: utf-8
import requests
from lxml import etree


class BookItem(dict):
    pass


class ChapterItem(dict):
    pass


def download(url, callback=None, **kwargs):
    resp = requests.get(url, timeout=10)
    resp.encoding = 'gbk'  # 在读取响应数据时，可以先指定字符集
    if resp.status_code == 200:
        if callback:
            callback(resp.text, **kwargs)
        else:
            parse(resp.text)
    else:
        print('%s 下载失败' % url)


def parse(html):
    root = etree.HTML(html)
    nav_list = root.xpath('//ul[@class="channel-nav-list"]/li/a')[:-1]
    for nav_a in nav_list:
        print(nav_a.get('href'), nav_a.text)
        download(nav_a.get('href'), parse_book)


def parse_book(html):
    root = etree.HTML(html)
    seeWell_lis = root.xpath('//ul[starts-with(@class,"seeWell")]/li')
    for seeWell_li in seeWell_lis:
        item = BookItem()
        item['cover_url'], item['name'] = seeWell_li.xpath('./a/img/@src | ./a/img/@alt')
        if item['cover_url'].find('nocover.jpg') > 0:
            item['cover_url'] = ''

        item['author'] = seeWell_li.xpath('./span/a[2]/text()')[0]
        item['info'] = seeWell_li.xpath('./span/em/text()')[0]
        item['info_url'] = seeWell_li.xpath('./span/a[last()]/@href')[0]

        itempipeline(item)

        download(item['info_url'],
                 parse_detail,
                 book_name=item['name'])


def parse_detail(html, book_name):
    root = etree.HTML(html)
    read_url = root.xpath('//div[@class="b-oper"]/a[1]/@href')[0]
    download(read_url, parse_chaps, book_name=book_name)


def parse_chaps(html, book_name):
    root = etree.HTML(html)
    chap_lis = root.xpath('//div[@class="clearfix dirconone"]/li')
    for chap_li in chap_lis:
        item = ChapterItem()
        item['title'], item['chap_url'] = chap_li.xpath('./a/@title | ./a/@href')
        item['book_name'] = book_name
        itempipeline(item)


def itempipeline(item):
    if isinstance(item, BookItem):
        print('---保存书信息--')
        print(item)

    else:
        print('---保存章节信息--')
        print(item)


if __name__ == '__main__':
    download('http://www.quanshuwang.com')
