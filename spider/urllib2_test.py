#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-30 13:58:05
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$

# coding=utf-8


import urllib2


url = "http://www.baidu.com/"

# User-Agent 是爬虫和反爬虫斗争的第一步
url_headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}

# 通过urllib2.Request构造一个请求对象
req = urllib2.Request(url, headers=url_headers)

# response 是返回服务器响应的类文件，除了支持文件的操作外，还支持以下常用的方法：
response = urllib2.urlopen(req)

# 返回HTTP的响应码，成功返回200，4 服务器页面出错，5 服务器本身问题
print response.getcode()

# 返回实际数据的实际url,防止重定向的问题
print response.geturl()

# 返回服务器响应的HTTP报头
print response.info()

# 打印响应内容
# print response.read()