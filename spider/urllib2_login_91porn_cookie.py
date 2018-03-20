#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-01 16:56:13
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$


import urllib
import urllib2
import cookielib
import re

url = ""
url2 = ""


# 通过CookieJar()类构建一个cookieJar()对象，用来保存cookie的值
cookie = cookielib.CookieJar()

# 通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie，参数就是构建的cookieJar()对象
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
proxyhandler = urllib2.ProxyHandler({"http":"61.155.164.109:3128"})

# 构建一个自定义的opener
opener = urllib2.build_opener(cookie_handler, proxyhandler)

# 通过自定义的opener的addheaders的参数，可以添加HTTP报头参数
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"), ("Connection", "keep-alive")]

# 获取 验证码
codeImg = opener.open(url2).read()
# print codeImg

fn = open("code.png", "wb")
fn.write(codeImg)
fn.close()

key = int(raw_input("请输入验证码: "))

# 需要登录的账户密码
data = {
    "username": "hugong2",
    "password": "wenjunai93",
    "captcha_input": key,
    "fingerprint": 563451053,
    "fingerprint2":"d53861a6015eaf888c921fc73f695e73",
    "action_login":"Log In",
    "session_language":"cn_CN",
    "x":51,
    "y":10
}

data = urllib.urlencode(data)

# post方式获取
request = urllib2.Request(url, data=data)

response = opener.open(request)

# 查找视频链接
link = re.search(r'<a  href="(.*?)"\s>视频', response.read())
url = link.group(1)

# 请求视屏页面
response = opener.open(url)

# 查找最近加精链接
link = re.search(r'<A href="(.*?)">最近加精</A>', response.read())

# 组合最近加精的url(网址)
basic_url = link.group(1) + "&page="

startpage = int(raw_input("请输入起始页:"))
endpage = int(raw_input("请输入结束页:"))


for i in range(startpage, endpage+1):
    # 组合需要爬取的最近加精的网址(翻页)
    src = basic_url + str(i)

    # 请求最近加精视频页面
    response = opener.open(src)
    needstr = response.read()

    # 查找当前页面最近加精的所有视屏的链接，返回一个list
    needstrs = re.findall(r'[\s\S]*?<div class="listchannel">([\s\S]*?)<div class="startratebox">', needstr)

    for i in needstrs:
        # 查找视屏的收藏值
        a = re.search(r"[\s\S]*收藏:</span>\s([0-9]*)", i)
        # 收藏大于多少才去爬取该视频链接
        if int(a.group(1)) > 1000:
            # print i
            
            url = re.search(r'<a target=blank href="(.*?)"\stitle="(.*?)">', i)
            Author = re.search(r'作者:</span>[\s\S]*?>(.*?)<', i)
            print url.group(2)
            print "--收藏:", int(a.group(1)), "作者:", Author.group(1)
            # print "src: ", url.group(1)
            src = url.group(1)

            # 请求该视频的播放页面
            response = opener.open(src)

            # 查找视屏播放(下载)链接
            src = re.search(r'<video[\s\S]*?<source src="(.*?)"\stype', response.read())
            print src.group(1)
            print 

