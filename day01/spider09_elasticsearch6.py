#!/usr/bin/python3
# coding: utf-8

from urllib.request import urlopen, Request

import json

# ES搜索引擎的地址
BASE_URL = 'http://119.3.170.97'


def add_index(index_name):
    url = BASE_URL + '/' + index_name
    params = {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 1
        }
    }

    # PUT
    resp = urlopen(Request(url,
                           json.dumps(params).encode('utf-8'),
                           headers={
                               'Content-Type': 'application/json'
                           }, method='PUT'))
    if resp.code == 200:
        bytes = resp.read()
        resp_json = json.loads(bytes.decode('utf-8'))
        print(resp_json)


def delete_index(index_name):
    url = BASE_URL + '/' + index_name
    resp = urlopen(Request(url, method='DELETE'))
    if resp.code == 200:
        bytes = resp.read()
        resp_json = json.loads(bytes.decode('utf-8'))
        print(resp_json)


def add_ip(index_name, type_name, id=None):
    url = BASE_URL + '/' + index_name + "/" + type_name + "/"
    if id:
        url += str(id)

    document = {
        'type': 'http',
        'host': '1.198.72.145',
        'port': '9999',
        'city': '河南'
    }

    resp = urlopen(Request(url,
                           json.dumps(document).encode('utf-8'),
                           {
                               'Content-Type': 'application/json'
                           }))
    if resp.code == 200:
        bytes = resp.read()
        resp_json = json.loads(bytes.decode('utf-8'))
        print(resp_json)


if __name__ == '__main__':
    # add_index('proxy_ips')
    # delete_index('proxy_ips')
    add_ip('proxy_ips', 'ips')
