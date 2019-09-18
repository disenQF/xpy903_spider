#!/usr/bin/python3
# coding: utf-8

from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from lxml import etree

def download(url):
    resp = urlopen(url)
    if resp.code == 200:
        bytes = resp.read()
        html = bytes.decode('utf-8')
        parse(html)


def parse(html):
    # lxml支持xpath提取数据的引擎etree
    root = etree.HTML(html)  # 解析html获取根元素对象

    # print(type(root))
    # print(dir(root))

    sons_elements = root.xpath('//div[@class="sons"]') # list[<Element>, ...]
    for sons_element in sons_elements:
        title = sons_element.xpath('.//p[1]//b/text()')  # list<'', ''>
        author = sons_element.xpath('.//p[2]/a/text()')

        content = sons_element.xpath('.//div[@class="contson"]/text()')
        if not title:
            break

        print(title[0], author[0], author[1])
        print(content)


if __name__ == '__main__':
    download('https://www.gushiwen.org/index.aspx')