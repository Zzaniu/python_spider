#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-30 14:14:29
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$

import urllib
import urllib2


url = "http://www.baidu.com/s"

headers = {"User-Agent" : "Mozilla..."}

keywd = raw_input("请输入要查找的关键字: ")

wd = {"wd" : keywd}
wd = urllib.urlencode(wd)

fullurl = url + "?" + wd
print fullurl

request = urllib2.Request(url, headers = headers)

response = urllib2.urlopen(request)

# print response.read()

