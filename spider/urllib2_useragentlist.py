#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-30 13:42:02
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$

import urllib2
import random


# 构造一个请求链接
url = "http://www.baidu.com/"

# 可以是User-Agent列表，也可以是代理列表
ua_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/5s.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0"
]

# 在User-Agent列表里随机选择一个User-Agent
user_agent = random.choice(ua_list)

# 构造一个请求
request = urllib2.Request(url)

# add_header()方法 添加/修改 一个HTTP报头
request.add_header("User-Agent", user_agent)

# get_header() 获取一个已有的HTTP报头的值，注意只有第一个字母大写，其余必须小写
print request.get_header("User-agent")





