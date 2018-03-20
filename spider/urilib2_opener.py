#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-30 21:37:10
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$

import urllib2


# 构建一个HTTPHandler处理器对象，支持处理HTTP的请求
# http_handler = urllib2.HTTPHandler()

# 在HTTPHandler增加参数"debuglevel=1"将会在佛那个打开Debug log模式，程序在执行的时候会打印收发包的信息
http_handler = urllib2.HTTPHandler(debuglevel=1)

# 调用build_opener()方法构建一个自定义的opener对象，参数是构建的处理器对象
opener = urllib2.build_opener(http_handler)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}
request = urllib2.Request("http://www.baidu.com/", headers=headers)

response = opener.open(request)

# print response.read()