#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-16 18:34:49
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$

import urllib
import urllib2
import cookielib
from lxml import etree
import cPickle


import sys
reload(sys)
sys.setdefaultencoding("utf8")




if __name__ == "__main__":
    url = "https://passport.weibo.cn/signin/login"
    data = {
        "username" : "451620411@qq.com",
        "password" : "!zaniuai93*",
        "savestate" : "1",
        "r" : "http://m.weibo.cn/?jumpfrom=wapv4&tip=1",
        "ec" : "0",
        "pagerefer" : "",
        "entry" : "mweibo",
        "wentry" : "",
        "loginfrom" : "",
        "client_id" : "",
        "code" : "",
        "qq" : "",
        "mainpageflag" : "1",
        "hff" : "",
        "hfp" : "",
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        "Connection": "keep-alive",
        "Referer": "https://passport.weibo.cn/signin/login",
        "Host": "passport.weibo.cn",
        "Origin": "https://passport.weibo.cn",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = urllib.urlencode(data)

    cookie = cookielib.CookieJar()

    cookie_handler = urllib2.HTTPCookieProcessor(cookie)

    opener = urllib2.build_opener(cookie_handler)

    opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"),("Connection", "keep-alive")]

    # req = urllib2.Request(url, data=data)

    req = urllib2.Request(url, data=data, headers = headers)

    # response = opener.open(req).read()

    response = urllib2.urlopen(req).read()

    if response.find("Zzaniu") >-1:
        print "login success...."
        with open("weibo_mobile_success.html", "w") as f:
            f.write(response)
    else:
        print "login fail...."
        with open("weibo_mobile_error.html", "w") as f:
            f.write(response)



