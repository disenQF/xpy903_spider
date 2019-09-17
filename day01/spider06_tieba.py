#!/usr/bin/python3
# coding: utf-8

from urllib.request import urlopen, Request
from urllib.parse import urlencode

import ssl

import time

ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://tieba.baidu.com/f'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Cookie': 'BAIDUID=9F7DC63DE89990C8A6573B62C378D96B:FG=1; BIDUPSID=9F7DC63DE89990C8A6573B62C378D96B; PSTM=1565793453; delPer=0; rsv_i=f8d3thm9XNy5y%2FwoIou1LOOhWBEbLFpAsrYrwUYq%2BVGFtiGC8blvw%2F1FZgm8G5WSgEyl2%2FSYvYD8Ia6sPaUYK5vw0C%2F8qwE; FEED_SIDS=940877_0915_16; H_WISE_SIDS=134725_126887_133103_100805_135965_136286_125579_120145_136238_132909_130763_132378_131517_118891_118862_118856_118830_118793_107316_133351_129654_136196_132250_127027_131861_128968_135308_135813_133847_132551_133287_135432_135874_129644_131423_134614_134028_135524_110085_136145_134152_127969_131752_131951_135672_135459_127417_135864_136304_134934_134352_135834_136261; H_PS_PSSID=29634_1436_21102_18559_29523_29521_29721_29567_29221; BCLID=8425945439445267515; PSINO=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=_6AsJeCCxG3jKXrwA-ryOXPhNa70GXVmYDdP3J; H_BDCLCKID_SF=tRk8oK-atDvHHPbY54rM2DCJ5fQfK4c2aIOt0TrJabC3SK_zKU6qLUtbQNbBaUR2b2bnVnv65U7fOl4m2MAhW4by0PQyJMIEtRk8oK-atDvHHPbY54rM2DCJ5fQfK4c2aIOt0TrJabC3Vp5MKU6qLUtbQNbBaUR2b5PeBMcS-nOxExAm2MAhW4by0PQyJMIEtJFDVIthfIP3jbIk-Pnfbtu_hgT22jni-jn9aJ5nJD_Msn7NKJjbKftV2xoBbtcK-gvlaMjOQpP-HJAGQ6JkhUR3DJ3P5x7WLC7pKl0MLncWbb0xyUQDMT0SQUnMBMn8teOnaITg3fAKftnOM46JehL3346-35543bRTohFLtD0bhKDle5Rb5nbHhfnaa47-bTrKBRu8a-oJbUACLJbkbftd2-teafnv-jvCs4oXBMnmjhrpjT3nWhKDWtObQTJZfD7H3KC-JI0MhM5; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1568691484; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1568701267; __yjsv5_shitong=1.0_7_0c4da3ab1870d0cce0d224ee336fd89e9e2a_300_1568701267081_223.255.14.197_6b3d55dd; yjs_js_security_passport=42df567f1aad41cdefa513570930246543247378_1568701267_js'
}

def download(page):
    params = {
        'kw': 'python3',
        'ie': 'utf-8',
        'pn': (page-1)*50
    }
    request = Request(url + "?" + urlencode(params),
                      method='GET',
                      headers=headers)

    resp = urlopen(request)
    if resp.code == 200:
        bytes = resp.read()
        print('开始保存第%s 页的数据' % page)
        save(bytes, page)

def save(bytes, page):
    with open('python3_%s.html' % page, 'wb') as f:
        f.write(bytes)

    print('第%s页数据保存成功!' % page)


if __name__ == '__main__':
    for page in range(1, 6):
        print('开始下载第%s 页' % page)
        download(page)

        time.sleep(3)

