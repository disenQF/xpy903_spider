#!/usr/bin/python3
# coding: utf-8

from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 下载html
url1 = 'http://www.baidu.com'
urlretrieve(url1, 'baidu.html')

# 下载图片
# url2 = 'http://upload.mobiletrain.org/2019/0815/1565834517474.png'
# urlretrieve(url2, '1565834517474.png')
