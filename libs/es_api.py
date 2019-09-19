#!/usr/bin/python3
# coding: utf-8
import uuid

import requests

"""
封装搜索引擎的各种操作
"""

BASE_URL = 'http://119.3.170.97/'


def add_index(index_name):
    # str.format()方法
    url = f'{BASE_URL}{index_name}'
    json = {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        }
    }

    try:
        resp = requests.put(url, json=json)
        ret = resp.json()
        print(ret)
        return ret['acknowledged']
    except:
        pass
    return False


def remove_index(index_name):
    resp = requests.delete(f'{BASE_URL}{index_name}')
    ret = resp.json()
    return ret['acknowledged']


def add_doc(index_name, type_name, **kwargs):
    if kwargs.get('id'):
        url = f'{BASE_URL}{index_name}/{type_name}/{kwargs["id"]}'
        kwargs.pop('id')
    else:
        url = f'{BASE_URL}{index_name}/{type_name}/'

    resp = requests.post(url, json=kwargs)
    ret = resp.json()
    return True


def update_doc(index_name, type_name, **kwargs):
    if kwargs.get('id'):
        url = f'{BASE_URL}{index_name}/{type_name}/{kwargs["id"]}'
        kwargs.pop('id')

        requests.put(url, json=kwargs)
        return True
    else:
        raise Exception('必须提供id参数')


def delete_doc(index_name, type_name, id):
    url = f'{BASE_URL}{index_name}/{type_name}/{id}'
    requests.delete(url)
    return True


def query(index_name, kw=None):
    url = f'{BASE_URL}{index_name}/_search'
    resp = requests.get(url, params={
        'q': (kw if kw else '')
    })

    ret = resp.json()
    hits = ret['hits']['hits']

    datas = []
    for source in hits:
        data = source['_source']
        data['id'] = source['_id']

        datas.append(data)

    return datas


if __name__ == '__main__':
    # print(add_index('books'))
    # remove_index('books')

    # add_index('books')
    # {'_index': 'books',
    #    '_type': 'book',
    #    '_id': '88c6438f133e49dbba619a602400d4ad'}

    item = {
        'id': '88c6438f133e49dbba619a602400d4ad',
        'name': 'Python高级爬虫',
        'author': 'Disen',
        'cover': '',
        'info': '非常实用的书'
    }

    # print(update_doc('books', 'book', **item))
    # print(delete_doc('books', 'book', '44f121d982134c89869878d4112f0079'))

    print(query('books', 'python'))
