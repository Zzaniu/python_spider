#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-30 22:23:15
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$

import urllib2

proxyswitch = True

# 构建一个Handler处理器对象，参数是一个字典类型，包括代理类型和代理服务器的IP+PORT
proxyhandler = urllib2.ProxyHandler({"http":"61.155.164.109:3128"})

# 构建了一个没有代理的处理器对象
nullproxyhandler = urllib2.ProxyHandler({})

if proxyswitch:
    opener = urllib2.build_opener(proxyhandler)
else:
    opener = urllib2.build_opener(nullproxyhandler)


opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"), ("Connection", "keep-alive")]
# 构建一个全剧的opener，之后所有的请求都可以用urlopen()方法去发送，也附带Handler的功能
urllib2.install_opener(opener)

request = urllib2.Request("http://www.baidu.com/")
response = urllib2.urlopen(request)
print response.read()