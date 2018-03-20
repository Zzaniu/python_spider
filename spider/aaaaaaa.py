#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-02 20:55:14
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$

import re
import random
import urllib
from PIL import Image
from pytesser import pytesser
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')


print os.path.join("./test", "temp")


# image = Image.open('code.png')



# img = Image.open('code.png')
# img = img.resize((120,54))
# img_grey = img.convert('L')

# threshold = 60
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
# img_out = img_grey.point(table, '1')

# img_out.save("code2.png")

# text = pytesser.image_to_string(img_grey)  # 将图片转成字符串
# print text





# image = Image.open('code.png')

# print image.size

# im = image.resize((120,54))

# im_new = im.convert("P")

# im_new.save("code1.png")

# # image = Image.open('12.png')

# # im = image.convert("L")

# # im.save("12_1.png")

# a = pytesser.image_file_to_string('456.jpg')

# print a

# print pytesser.image_file_to_string('zimu.jpg')

# while True:
#     print pytesser.image_to_string(im_new)

#     a = raw_input("请输入： ")
#     if "y" == a:
#         print "*"*50
#         break


# strs = None
# with open("91_porn.txt", "r") as f:
#     strs = f.read()

# a = 0

# url = re.findall(r'(--收藏:(\d+)[\s\S]*?rf)', strs)
# for i,m in url:
#     if int(m) > 15500:
#         print i
#         print
#         a += 1

# print "共%d条"%a

# with open("91_11111.html", "r") as f:
#     strs = f.read()

# list_url = re.findall(r'[^<a.*?]<img\ssrc=".*?"\sfile="(.*?)"' ,strs)
# for i in list_url:
#     print i


# num_list = [0,1,2,3,4,5,6,7,8,9]

# num = random.choice(num_list)
# print num

# import spynner  
# import pyquery  
# import time  
# import BeautifulSoup  
# import sys  
# from scrapy.http import HtmlResponse  
# class WebkitDownloaderTest( object ):  
#     def process_request( self, request, spider ):  
# #        if spider.name in settings.WEBKIT_DOWNLOADER:  
# #            if( type(request) is not FormRequest ):  
#                 browser = spynner.Browser()  
#                 browser.create_webview()  
#                 browser.set_html_parser(pyquery.PyQuery)  
#                 browser.load(request.url, 20)  
#                 try:  
#                         browser.wait_load(10)  
#                 except:  
#                         pass  
#                 string = browser.html  
#                 string=string.encode('utf-8')  
#                 renderedBody = str(string)  
#                 return HtmlResponse( request.url, body=renderedBody ) 
                

