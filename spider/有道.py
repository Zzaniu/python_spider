#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-30 17:06:52
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$

import urllib
import urllib2


key = raw_input("请输入想要翻译的数据： ")

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }
data = {
    "i":key,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"1514623668324",
    "sign":"01d12dc7d69d323061a455567f725d30",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTIME",
    "typoResult":"false"
}

data = urllib.urlencode(data)
print data

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule HTTP/1.1"

request = urllib2.Request(url, data, headers)

response = urllib2.urlopen(request)

print response.read()
