#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-30 12:31:12
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$

import urllib2

url = "http://www.baidu.com/"
ua_headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
}
req = urllib2.Request(url, headers=ua_headers)

response = urllib2.urlopen(req)
print response.read()
