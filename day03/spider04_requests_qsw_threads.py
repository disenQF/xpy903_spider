#!/usr/bin/python3
# coding: utf-8
import requests
from lxml import etree

from threading import Thread
from queue import Queue

# from multiprocessing import Process
# from multiprocessing import Queue, Pipe, Manager


class BookItem(dict):
    pass


class ChapterItem(dict):
    pass

class DownloaderThread(Thread):
    def __init__(self, tasks_queue, result_queue):
        super().__init__()
        self.tasks: Queue = tasks_queue  # 下载任务队列
        self.results: Queue = result_queue # 下载结果队列

    def run(self):
        while True:
            try:
                # url, callback, **kwargs
                # 获取下载任务
                url, *callback_params = self.tasks.get(timeout=30)

                if len(callback_params) == 0:
                    self.download(url)
                elif len(callback_params) == 1:
                    self.download(url, callback_params[0])
                else:
                    self.download(url, callback_params[0], **callback_params[1])

            except Exception as e:
                print(e)
                break

        print('--下载任务完成--')

    def download(self, url, callback=None, **kwargs):
        resp = requests.get(url, timeout=10)
        resp.encoding = 'gbk'  # 在读取响应数据时，可以先指定字符集
        if resp.status_code == 200:
            if callback:
                # callback(resp.text, **kwargs)
                self.results.put((resp.text, callback, kwargs))
            else:
                # parse(resp.text)
                self.results.put((resp.text, ))
        else:
            print('%s 下载失败' % url)


class ParserThread(Thread):
    def __init__(self, tasks_queue, results_queue, items_queue):
        super(ParserThread, self).__init__()
        self.results: Queue = results_queue
        self.items: Queue = items_queue
        self.tasks: Queue = tasks_queue

    def run(self):
        while True:
            try:
                html, *callback_params = self.results.get(timeout=30)
                if len(callback_params) == 0:
                    self.parse(html)

                elif len(callback_params) >= 1:
                    callback = callback_params[0] # str
                    f = eval(callback)

                    if len(callback_params) == 1:
                        f(html)
                    else:
                        kwargs = callback_params[1]
                        f(html, **kwargs)
            except:
                break

        print('---解析任务完成--')

    def parse(self, html):
        root = etree.HTML(html)
        nav_list = root.xpath('//ul[@class="channel-nav-list"]/li/a')[:-1]
        for nav_a in nav_list:
            print(nav_a.get('href'), nav_a.text)
            self.tasks.put((nav_a.get('href'), 'self.parse_book'))

    def parse_book(self, html):
        root = etree.HTML(html)
        seeWell_lis = root.xpath('//ul[starts-with(@class,"seeWell")]/li')
        for seeWell_li in seeWell_lis:
            item = BookItem()
            item['cover_url'], item['name'] = seeWell_li.xpath('./a/img/@src | ./a/img/@alt')
            if item['cover_url'].find('nocover.jpg') > 0:
                item['cover_url'] = ''

            item['author'] = seeWell_li.xpath('./span/a[2]/text()')[0]
            item['info'] = seeWell_li.xpath('./span/em/text()')[0]
            item['info_url'] = seeWell_li.xpath('./span/a[last()]/@href')[0]

            self.items.put(item)  # 将数据存入数据处理队列中

            # 将新的下载任务存放到下载任务队列中
            self.tasks.put((item['info_url'],
                            'self.parse_detail',
                            {'book_name':item['name']}))

    def parse_detail(self, html, book_name):
        root = etree.HTML(html)
        read_url = root.xpath('//div[@class="b-oper"]/a[1]/@href')[0]
        self.tasks.put((read_url, 'self.parse_chaps', {'book_name':book_name}))

    def parse_chaps(self, html, book_name):
        root = etree.HTML(html)
        chap_lis = root.xpath('//div[@class="clearfix dirconone"]/li')
        for chap_li in chap_lis:
            item = ChapterItem()
            item['title'], item['chap_url'] = chap_li.xpath('./a/@title | ./a/@href')
            item['book_name'] = book_name
            self.items.put(item)


class ItemThread(Thread):
    def __init__(self, items_queue):
        super(ItemThread, self).__init__()
        self.items: Queue = items_queue

    def run(self):
        while True:
            try:
                item = self.items.get(timeout=60)
                self.itempipeline(item)
            except:
                break

        print('-------')

    def itempipeline(self, item):
        if isinstance(item, BookItem):
            print('---保存书信息--')
            print(item)

        else:
            print('---保存章节信息--')
            print(item)


if __name__ == '__main__':
    # download('http://www.quanshuwang.com')
    tasks_queue = Queue()
    result_queue = Queue()
    items_queue = Queue()

    tasks_queue.put(('http://www.quanshuwang.com', ))

    downloader = DownloaderThread(tasks_queue, result_queue)
    downloader.start()

    parser = ParserThread(tasks_queue, result_queue, items_queue)
    parser.start()

    itempipeline = ItemThread(items_queue)
    itempipeline.start()

    downloader.join()
    parser.join()
    itempipeline.join()

    print('---over----')
