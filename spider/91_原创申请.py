#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-02 23:32:08
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$

import urllib
import urllib2
import re
from lxml import etree

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}


def start_work(url, start_page, end_page):
    for i in range(start_page, end_page+1):
        if 0 == i:
            fullurl = url
        else:
            fullurl = url + "&page=" + str(i)
        dealurl(fullurl)


def dealurl(url):
    print "28-url = ", url
    request = urllib2.Request(url, headers=headers)
    html = urllib2.urlopen(request).read()
    content = etree.HTML(html)
    list_id = content.xpath('//tbody/tr/th[@class="subject new"]/span/@id')
    link_lists_url = []
    for i in list_id:
        i = i.replace("thread", "normalthread")
        link_lists_ding = content.xpath('//tbody[@id="%s"]/tr/th/font'%i)
        if [] == link_lists_ding:
            continue

        int_beiding = re.search(r"\d+", link_lists_ding[0].text)
        if int_beiding.group() > 100:
            link_lists_url_temp = content.xpath('//tbody[@id="%s"]/tr/th/span/a/@href'%i)

            link_lists_url.append(link_lists_url_temp[0].split("&page")[0])

    link_lists_url = set(link_lists_url)
    for sub_url in link_lists_url:
        print "sub_url = ", sub_url
        url = "http://f.91p11.space/" + sub_url
        dealImageUrl(url)


def dealImageUrl(url):
    print "54-url = ", url
    request = urllib2.Request(url, headers=headers)
    html = urllib2.urlopen(request).read()
    list_filename = re.findall(r'[^<a.*?]<img\ssrc=".*?"\sfile="(.*?)"', html)
    for src in list_filename:
        fullsrc = "http://f.91p11.space/" + src
        loadImage(fullsrc)


def loadImage(url):
    request = urllib2.Request(url, headers=headers)
    image = urllib2.urlopen(request).read()
    filename = url[-20:]
    full_filename = "./Image/" + filename
    with open(full_filename, "wb") as f:
        f.write(image)


if __name__ == "__main__":
    url = ""
    start_page = int(raw_input("请输入起始页面: "))
    end_page = int(raw_input("请输入结束页面: "))
    start_work(url, start_page, end_page)
    dealurl(url)
