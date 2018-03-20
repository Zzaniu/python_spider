# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class TencentspiderPipeline(object):
    def __init__(self):
        self.filename = open("Tencent.json", "w")
    def process_item(self, item, spider):
        text = json.dumps(dict(item), ensure_ascii = False).encode("utf-8") + '\n'
        self.filename.write(text)
        return item

    def close_spider(self, spider):
        self.filename.close()
