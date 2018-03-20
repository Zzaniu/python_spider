#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 13:59:40
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$


import re

a = '''<li>公司名称：<span>泗县豪翔体育用品有限公司</span></li>'''

try:
    list_url = re.search('公司名称.*?>(.*?\(.*\)).*?<', a).group(1)
except:
    list_url = re.search('公司名称.*?>(.*?)<', a).group(1)
print list_url

a = """<th style="color:#ff7300" >公司成立时间：</th>
<td>2014-07-03</td>"""
list_url = re.search('公司成立时间.*?>.*?>(.*?)<', a).group(1)
print list_url

print "end!!!"

