#!/usr/bin/python3
# coding: utf-8
import re
import urllib.request as req
from http.client import HTTPResponse

# 目标
url = 'http://www.mobiletrain.org/?pinzhuanbdtg=biaoti'

# 下载
response: HTTPResponse = req.urlopen(url)

# 验证下载(请求)是否成功
if response.code == 200:
    print(response.geturl(), '请求成功!')
    # 读取所有的内容
    data = response.readlines()  # [b'', b'', ...]

    # 读取响应数据的编码
    print(response.headers, type(response.headers))  # http.client.HTTPMessage
    print(response.headers.get('Content-Type'))

    # 读取每行的数据
    encoding = 'utf-8'

    for line in data:
        # 尝试查找字符集 charset="UTF-8"
        content_charset = re.findall(br'charset="(.+)"', line)
        if content_charset:
            encoding = content_charset[0].decode(encoding='utf-8')
            break

    print('从内容中查找到了字符串charset=', encoding)
    # 将list内容转成字节字母串
    bytes = b''.join(data)
    print(bytes.decode(encoding))