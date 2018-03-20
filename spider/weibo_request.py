#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-17 18:46:10
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$


from pytesser import pytesser
from selenium import webdriver
from lxml import etree
import requests
import pickle
import time
import os
import sys


reload(sys)
sys.setdefaultencoding('utf-8')




def get_cookie_from_network():
    url_login = 'https://passport.weibo.cn/signin/login' 
    driver = webdriver.Chrome()
    driver.get(url_login)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="loginName"]').send_keys('451620411@qq.com') # 改成你的微博账号
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="loginPassword"]').send_keys('!zaniuai93*') # 改成你的微博密码
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="loginAction"]').click() # 点击登录
    time.sleep(3)
    # 获得 cookie信息
    cookie_list = driver.get_cookies()
    print cookie_list
    driver.quit()

    cookie_dict = {}
    for cookie in cookie_list:
        #写入文件
        f = open(cookie['name']+'.weibo','w')
        pickle.dump(cookie, f)
        f.close()

        if cookie.has_key('name') and cookie.has_key('value'):
            cookie_dict[cookie['name']] = cookie['value']

    return cookie_dict


def get_cookie_from_cache():
    cookie_dict = {}
    for parent, dirnames, filenames in os.walk('./'):
        print "parent = ", parent
        print "dirnames = ", dirnames
        print "filenames = ", filenames
        for filename in filenames:
            if filename.endswith('.weibo'):
                print filename
                with open(filename, 'r') as f:
                    d = pickle.load(f)

                    if d.has_key('name') and d.has_key('value') and d.has_key('expiry'):
                        expiry_date = int(d['expiry'])
                        if expiry_date > (int)(time.time()):
                            cookie_dict[d['name']] = d['value']
                        else:
                            return {}

    return cookie_dict


def  get_cookie():
    cookie_dict = get_cookie_from_cache()
    if not cookie_dict:
        cookie_dict = get_cookie_from_network()
    
    return cookie_dict


def get_weibo_list(url):
    cookdic = get_cookie()

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36'}
    timeout = 5
    r = requests.get(url, headers=headers, cookies=cookdic,timeout=timeout).text
    with open("weibo_request.html", "w") as f:
        f.write(r)
    

if __name__ == "__main__":
    get_weibo_list("https://m.weibo.cn/u/5721826695?uid=5721826695&luicode=20000174")