#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-01 16:56:13
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$


import threading
import urllib
import urllib2
import cookielib
from PIL import Image
from pytesser import pytesser
from selenium import webdriver
from lxml import etree
import re
import sys

#reload(sys)
#sys.setdefaultencoding('utf8')


# 创建锁
mutex = threading.Lock()

def deal_url(url):
    response = opener.open(url)
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
            mutex.acquire()
            print url.group(2)
            print "--收藏:", int(a.group(1)), "作者:", Author.group(1)

            src = url.group(1)
            print "src = ", src
            print
            mutex.release()

            # 请求该视频的播放页面
            # response = opener.open(src)
            #
            # # 查找视屏播放(下载)链接
            # src = re.search(r'<video[\s\S]*?<source src="(.*?)"\stype', response.read())
            # print src.group(1)
            # print


if __name__ == "__main__":
    url = ""
    url2 = ""

    # 利用cookie，免除登陆
    # filenameOfCookie = 'renren_cookie.txt'
    # cookie = http.cookiejar.MozillaCookieJar(filenameOfCookie)
    # headler = urllib.request.HTTPCookieProcessor(cookie)
    # opener = urllib.request.build_opener(headler)

    # 通过CookieJar()类构建一个cookieJar()对象，用来保存cookie的值
    # cookie = cookielib.CookieJar()


    # 保存cookie的本地磁盘文件名
    filename = 'cookie.txt'
    # 声明一个MozillaCookieJar(有save实现)对象实例来保存cookie，之后写入文件
    cookiejar = cookielib.MozillaCookieJar(filename)
    # 使用HTTPCookieProcessor()来创建cookie处理器对象，参数为CookieJar()对象
    handler = urllib2.HTTPCookieProcessor(cookiejar)
    # 通过 build_opener() 来构建opener
    opener = urllib2.build_opener(handler)

    # # 通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie，参数就是构建的cookieJar()对象
    # cookie_handler = urllib2.HTTPCookieProcessor(cookie)

    # # 构建一个Handler处理器对象，参数是一个字典类型，包括代理类型和代理服务器的IP+PORT
    # # proxyhandler = urllib2.ProxyHandler({"http": "61.155.164.109:3128"})

    # # 构建一个自定义的opener
    # opener = urllib2.build_opener(cookie_handler)

    # 通过自定义的opener的addheaders的参数，可以添加HTTP报头参数
    opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"),("Connection", "keep-alive")]

    code_count = 0
    while True:
        code_count += 1
        # 获取 验证码
        codeImg = opener.open(url2).read()
        # print codeImg

        with open("code.png", "wb") as f:
            f.write(codeImg)

        image = Image.open('code.png')

        im = image.resize((120, 54))

        img_grey = im.convert('L')

        threshold = 60
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        img_out = img_grey.point(table, '1')

        img_out.save('code111.png')

        value = pytesser.image_to_string(img_out).strip()

        # im_new = im.convert("P")

        # value = pytesser.image_to_string(im_new).strip()
        print "识别出来的验证码是: ", value
        sys.exit(-1)
        print"nihao"
        print value.isdigit()
        print 4 == len(value)

        if value.isdigit() and 4 == len(value):
            key = int(value)
            print "已识别验证码%d张，验证码识别成功..."%code_count
            print "验证码是:", key

            break

    driver = webdriver.Chrome()
    driver.get(url)
    html = driver.page_source
    content = etree.HTML(html)
    finger_value = content.xpath(r'//p/input[@name="fingerprint"]/@value')[0]
    finger_value = int(finger_value)
    finger2_str = content.xpath(r'//p/input[@name="fingerprint2"]/@value')[0]
    finger2_str = finger2_str.encode('utf-8')
    driver.quit()

    # 需要登录的账户密码
    data = {
        "username": "hugong2",
        "password": "wenjunai93",
        "captcha_input": key,
        "fingerprint": finger_value,
        "fingerprint2": finger2_str,
        "action_login": "Log In",
        "session_language": "cn_CN",
        "x": 51,
        "y": 10
    }

    data = urllib.urlencode(data)

    # post方式获取
    request = urllib2.Request(url, data=data)

    response = opener.open(request)
    # 保存cookie到本地文件
    cookiejar.save()

    #print "response.read() = ", response.read()

    response_str = response.read()

    if response_str.find("hugong2") > -1:
        print "登陆成功..."
    else:
        print "登陆失败..."
        print response_str
        sys.exit(-1)

    # 查找视频链接
    link = re.search(r'<a\s\shref="(.*?)"\s>视频', response_str)
    url = link.group(1)
    print "视频url = ", url 

    # 请求视屏页面
    response = opener.open(url)
    response_str = response.read()

    if response_str.find("hugong2") > -1:
        print "登陆成功......"
    else:
        print "登陆失败......"
        print response_str
    sys.exit(-1)


    # 查找最近加精链接
    link = re.search(r'<A href="(.*?)">最近加精</A>', response_str)

    # 组合最近加精的url(网址)
    basic_url = link.group(1) + "&page="

    startpage = int(raw_input("请输入起始页:"))
    endpage = int(raw_input("请输入结束页:"))
    for i in range(startpage, endpage + 1):
        # 组合需要爬取的最近加精的网址(翻页)
        src = basic_url + str(i)

        t = threading.Thread(target=deal_url, args=(src,))
        t.start()
        if endpage == i:
            t.join()
