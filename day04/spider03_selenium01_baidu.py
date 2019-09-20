#!/usr/bin/python3
# coding: utf-8
import random
import time
from selenium.webdriver import Chrome

# 创建chrome的浏览器，并打开的
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC

chrome = Chrome('driver/chromedriver')

def start():

    # 打开baidu.com
    chrome.get('http://www.baidu.com')

    title = chrome.title
    title2 = chrome.find_element_by_css_selector('title').text
    title2 = chrome.find_element_by_xpath('//title').text
    print(title, title2, sep='\n')

    # 搜索"docker es集群"
    kwElement: WebElement = chrome.find_element_by_id('kw')
    kwElement.send_keys('docker es集群')

    time.sleep(1)
    chrome.find_element_by_id('su').click()

    cnt = 1
    exit_cnt = random.randint(10, 100)

    # 等待  class="nums_text"  元素出现
    ui.WebDriverWait(chrome, 10).until(
        EC.visibility_of_all_elements_located((By.CLASS_NAME, 'nums_text'))
    )

    while True:
        parse()

        # 点击下一页
        chrome.find_element_by_css_selector('#page').find_element_by_xpath('./a[last()]').click()
        cnt += 1
        if cnt > exit_cnt:
            break

        time.sleep(2)


    time.sleep(5)
    chrome.quit()  # chrome.close()

def parse():


    total = chrome.find_element_by_class_name('nums_text').text
    print(total)

    content = chrome.find_element_by_id('content_left')
    h3_list = content.find_elements_by_tag_name('h3')
    for h3Element in h3_list:
        a = h3Element.find_element_by_xpath('./a')
        href, title = a.get_attribute('href'), a.text
        print(href, title)

if __name__ == '__main__':
    start()