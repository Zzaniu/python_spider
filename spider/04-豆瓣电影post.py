#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-30 18:14:16
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$

import urllib
import urllib2

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend"


limitpage = raw_input("请输入要显示的数量: ")
startpage = raw_input("请输入起始页面: ")

data = {
    "page_limit":limitpage,
    "page_start":startpage
}
data = urllib.urlencode(data)
print data

fullurl = url

headers = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

request = urllib2.Request(fullurl, data, headers)
print urllib2.urlopen(request).read()
