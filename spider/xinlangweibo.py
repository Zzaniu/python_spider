#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-16 00:40:24
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$

import urllib
import urllib2
import cookielib
from PIL import Image
from pytesser import pytesser
from selenium import webdriver
from lxml import etree
import re
import time
import sys
import cPickle


reload(sys)
sys.setdefaultencoding('utf-8')




if __name__ == "__main__":
    url = "https://login.sina.com.cn/signup/signin.php?entry=sso"

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(1)

    try:
        driver.find_element_by_xpath('//*[@id="username"]').send_keys("451620411@qq.com")
        print 'user success!'
    except:
        print 'user error!'

    try:
        driver.find_element_by_xpath('//*[@id="password"]').send_keys("!zaniuai93*")
        print 'user success!'
    except:
        print 'user error!'

    time.sleep(1) 

    # try:
    #     #driver.find_element_by_xpath('//*[@id="remLoginName"]').click()
    #     #driver.find_element_by_xpath('//*[@id="vForm"]/div[2]/div/ul/li[6]/div/label').click()
    #     print 'user success!'
    # except:
    #     print 'user error!'

    # time.sleep(1) 

    try:
        driver.find_element_by_xpath('//*[@id="vForm"]/div[2]/div/ul/li[7]/div[1]/input').click()
        print 'user success!'
    except:
        print 'user error!'

    time.sleep(3) 

    # try:
    #     driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[3]/ul/li[1]/a/span[1]').click()
    #     print 'user success!'
    # except:
    #     print 'user error!'

    # time.sleep(3) 

    print driver.get_cookies()

    cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()]
    cookiestr = ';'.join(item for item in cookie)  
    print cookiestr 
    headers = {'cookie':cookiestr}
    # all_handles = driver.window_handles
    # handle_xinlang = driver.current_window_handle
    # for handle  in all_handles:
    #     if handle != handle_xinlang:
    #         driver.switch_to.window(handle)
    homeurl = driver.current_url
    print 'homeurl: %s' % homeurl
    # print int()

    driver.quit()
    cookie = cookielib.CookieJar()
    cookie_handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(cookie_handler)
    opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"),("Connection", "keep-alive")]
    req = urllib2.Request(homeurl, headers = headers)
    print "type(req) = ", type(req)

    response = opener.open(req)
    cookieStr = ""
    for item in cookie:
        cookieStr = cookieStr + item.name + "=" + item.value + ";"
    print "cookieStr = ", cookieStr
    html = response.read()
    with open("xinlang.html", "w") as f:
        f.write(html)

    # with open("xinlang.html", "w") as f:
    #     f.write(html)

    # context = etree.HTML(html)
    # url = context.xpath("/html/body/div[4]/div[1]/div[3]/ul/li[1]/a/@href")
    # print url

    url = "http://weibo.com"
    req = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(req)
    html = response.read()
    if html.find("Zzaniu") > -1:
        print "success..."
        with open("weibo.html", "w") as f:
            f.write(html)
    else:
        print "error..."

    # url = "https://weibo.com/aj/mblog/fsearch?ajwvr=6&pre_page=1&page=1&end_id=1516090968509985&min_id=4196706926526874&pagebar=1&unread_max_id=1516090968509970&unread_since_id=1516090968509970&__rnd=1516090985405"
    # req = urllib2.Request(url, headers = headers)
    # response = opener.open(req)
    # html = response.read()
    # if html.find("Zzaniu") > -1:
    #     print "success..."
    #     with open("weibo.txt", "w") as f:
    #         f.write(html)
    # else:
    #     print "error..."


    # # 通过CookieJar()类构建一个cookieJar()对象，用来保存cookie的值
    # cookie = cookielib.CookieJar()

    # # 通过HTTPCookieProcessor()处理器类构建一个处理器对象，用来处理cookie，参数就是构建的cookieJar()对象
    # 