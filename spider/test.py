#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-21 13:59:40
# @Author  : Zzaniu (Zzaniu@126.com)
# @Link    : http://example.org
# @Version : $Id$

import os
from aip import AipOcr
import json	
from PIL import Image
from pytesser import pytesser


APP_ID = '10725347'
API_KEY = 'XDsaGAzTlS24xNRi9Zx2000x'
SECRET_KEY = 'pBCMTYt3aekfQaG52qHgY95Ghae4mQZf'

aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

filePath = "code3.png"
# filePath = "captcha.png"

def get_file_content(filePath):
	with open(filePath, 'rb') as f:
		return f.read()

options = {
	'detect_direction' : 'ture',
	'language_type' : 'CHN_ENG',
}


result = aipOcr.basicGeneral(get_file_content(filePath), options)
# print type(result['words_result'][0]['words'].encode('utf-8'))
print (json.dumps(result).decode("unicode-escape"))

print os.getcwd()
print 

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
value = pytesser.image_to_string(img_out).strip()
print "value = ", value