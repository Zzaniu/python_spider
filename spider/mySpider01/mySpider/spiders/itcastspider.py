#!/usr/bin/env python
# -*- coding: utf-8 -*-


import scrapy
from mySpider.items import MyspiderItem


# 创建一个爬虫类
class ItcastSpider(scrapy.Spider):
    # 爬虫名
    name = "itcast"
    # 允许爬虫作用的范围
    allowd_domains = ["http://www.itcast.cn/"]
    # 爬虫其实的url
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]


    def parse(self, response):
        #with open("teacher.html", "w") as f:
            #f.write(response.body)
        # 通过scrapy自带的xpath匹配出所有老师的根节点列表集合
        teacher_list = response.xpath('//div[@class="li_txt"]')
        #teacheritem = []
        # 遍历根节点集合
        for each in teacher_list:
            # item对象用来保存数据的
            item = MyspiderItem()
            # extract() 将匹配出来的结果转换为Uincode字符串
            # 不加extract()结果为xpath对象
            name = each.xpath('./h3/text()').extract()

            title = each.xpath('./h4/text()').extract()

            info =  each.xpath('./p/text()').extract()
            
            item['name'] = name[0].encode("utf-8")
            item['title'] = title[0].encode("utf-8")
            item['info'] = info[0].encode("utf-8")

            # yield的内容，如果是数据给管道文件
            yield item
            #teacheritem.append(item)

            #print name[0]
            #print title[0]
            #print info[0]

        #return teacheritem


