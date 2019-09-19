#!/usr/bin/python3
# coding: utf-8

import requests

from ydm import ydm_api

session = requests.session()

def get_code():
    code_url = 'https://so.gushiwen.org/RandCode.ashx'
    # 下载验证码图片到本地文件中
    resp = session.get(code_url)
    print(resp.cookies)

    with open('code.png', 'wb') as f:
        f.write(resp.content)

    # 将本地验证图片文件路径 传给云打码的sdk方法，并从sdk方法中读取到验证码
    code = ydm_api('code.png')

    # 返回验证码
    return code


def login():
    url = 'https://so.gushiwen.org/user/login.aspx'
    data = {
        'email': '610039018@qq.com',
        'pwd': 'disen8888',
        'code': get_code()
    }

    resp = session.post(url, data)
    with open('gsh_logined.html', 'w') as f:
        f.write(resp.text)


if __name__ == '__main__':
    login()