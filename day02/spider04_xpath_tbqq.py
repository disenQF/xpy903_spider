#!/usr/bin/python3
# coding: utf-8
import re

import time

from request import get, save_file
from lxml import etree

BASE_URL = 'http://www.tbqq.net/'

def download(url):
    resp = get(url)
    content_type = resp.headers.get('Content-Type')

    charset = re.findall(r'(gbk|gbk2312|utf-8)', content_type, re.I)[0]

    if resp.code == 200:
        html = resp.read().decode(charset)
        parse(html)

def parse(html):
    root = etree.HTML(html)
    li_elements = root.xpath('//li[starts-with(@class,"deanactions")]')

    for li_element in li_elements:
        item = {}

        cover_url = li_element.xpath('./div[1]//img/@src')[0]
        item['cover_url'] = BASE_URL+cover_url

        item['name'] = li_element.xpath('.//div[@class="deanmadouname"]//text()')[0]
        zhiye = li_element.xpath('.//div[@class="deanmadouzhiye"]//text()')[-1]
        city = li_element.xpath('.//div[@class="deanmadouinfos"]/div[5]/text()')[0]
        city = city.strip()[4:]

        height_weight_list = li_element.xpath('.//div[@class="deanmadouinfos"]/div[2]/div[1]//text()')
        height, weight = height_weight_list[0], height_weight_list[2]

        star = li_element.xpath('.//div[@class="deanmadouinfos"]/div[2]/div[2]/span/text()')[0]

        save(item)

    time.sleep(0.5)
    #  下一页
    next_page = root.xpath('//a[@class="nxt"]/@href')[0]
    download(BASE_URL + next_page)


def save(item):
    # 将数据写入数据库中或es中

    # 下载图片，图片的文件名是模特名
    filename = item['name']+".jpg"
    save_file(item['cover_url'], "images/"+filename)



if __name__ == '__main__':
    url = 'http://www.tbqq.net'
    download(url)



