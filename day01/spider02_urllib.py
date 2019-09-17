#!/usr/bin/python3
# coding: utf-8
from urllib.request import urlopen

'''
Python3.6遇到的安全证书验证问题
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:749)>
'''
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 经过检验：  js动态反爬-Selenium
url = 'https://sou.zhaopin.com/?jl=530&kw=python&kt=3'

resp = urlopen(url) # http.client.HTTPResponse
if resp.code == 200:
    body = resp.read()  # byte 字节码
    # print(body)
    print(resp.headers.get('Content-Type'))  # text/html; charset=utf-8
    # print(body.decode('utf-8'))
    # 将响应的body写入文件中
    with open('zhaopin_python.html', mode='wb') as f:
        f.write(body)
