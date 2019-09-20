#!/usr/bin/python3
# coding: utf-8
import random

# 自定义UA池
user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/76.0.3809.132 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Window10) AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/76.0.3809.132 IE/537.36',
    'Mozilla/5.0 (Macintosh; Intel Android) AppleWebKit/537.36 (KHTML, like Gecko)'
    ' WebKit/76.0.3809.132',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) '
    'Gecko/20100101 Firefox/68.0',
]

def get():
    return random.choice(user_agent_list)