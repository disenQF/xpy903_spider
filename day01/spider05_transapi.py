#!/usr/bin/python3
# coding: utf-8

url = 'https://fanyi.baidu.com/transapi'
data = {
    'from': 'en',
    'to': 'zh',
    'query': 'apple',
    'source': 'txt'
}

'''
{
	"status": 0,
	"from": "en",
	"to": "zh",
	"type": 1,
	"version": 1,
	"result": "{\"content\":[{\"mean\":[{\"pre\":\"n.\",\"cont\":{\"\\u82f9\\u679c\":0}}]}],\"voice\":[{\"en_phonic\":\"[\\u02c8\\u00e6pl]\"},{\"us_phonic\":\"[\\u02c8\\u00e6pl]\"}],\"src\":\"apple\"}"
}
'''