#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-30 14:52:16
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$

import urllib
import urllib2



def writefile(data, filename):
    """
        filename:处理文件
    """
    filename = filename.decode("utf-8")
    print "正在写入..."
    with open(filename, "w") as f:
        f.write(data)


def urlopen(url):
    """
        url:要爬取的url地址
    """
    ua_headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }
    request = urllib2.Request(url, headers=ua_headers)
    response = urllib2.urlopen(request)
    return response.read()



def tiebaspider(url, beginpage, endpage, tieba):
    """
        url:要爬取的url地址
    """
    for pn in range(beginpage, endpage + 1):
        fullurl = url + "&pn=" + str(pn)
        filename = tieba + "第" + str(pn) + "页.html"
        print filename
        print fullurl
        data = urlopen(fullurl)
        writefile(data, filename)












if __name__ == "__main__":
    tieba = raw_input("请输入要爬取的贴吧： ")
    beginpage = int(raw_input("请输入起始页： "))
    endpage = int(raw_input("请输入结束页： "))
    url = urllib.urlencode({"kw":tieba})
    fullurl = "https://tieba.baidu.com/f?" + url
    tiebaspider(fullurl, beginpage, endpage, tieba)


