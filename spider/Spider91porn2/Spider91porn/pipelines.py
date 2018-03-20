# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import os


class Spider91PornPipeline(object):

    datainfo_list = []

    def __init__(self):
        self.filename = open("./Image/91porn.txt", "w")

    def process_item(self, item, spider):
        #print "item['datainfo'] = ", item["datainfo"]
        if item["datainfo"] not in Spider91PornPipeline.datainfo_list:
            Spider91PornPipeline.datainfo_list.append(item["datainfo"])
            #print "Spider91PornPipeline.datainfo_list = ", Spider91PornPipeline.datainfo_list
            self.filename.write(item["datainfo"])

        pathname = "./Image/" + item['roomname']
        if (not os.path.exists(pathname)):
            os.makedirs(pathname)
        filename = item['roomname'] + item['name'][-10:]
        #print "filename = ", filename
        with open(pathname + "/" + filename, "wb") as f:
            f.write(item['image'])
        #return item

    def close_spider(self, spider):
        self.filename.close()

