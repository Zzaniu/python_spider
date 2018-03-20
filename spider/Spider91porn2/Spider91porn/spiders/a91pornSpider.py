# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Spider91porn.items import Spider91PornItem 
import sys 
import re


reload(sys)
sys.setdefaultencoding('utf8')


class A91pornspiderSpider(CrawlSpider):
    name = '91pornSpider'
    allowed_domains = ['93.t9p.today']
    start_urls = ['http://93.t9p.today/forumdisplay.php?fid=19']

    pagelink = LinkExtractor(allow=r"fid=19&page=\d+")

    rules = (
        Rule(pagelink, callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        # response.xpath返回一个类 SelectorList 的实例，需要通过extract()方法解析
        # list_id = response.xpath('//tbody/tr/th[@class="subject new"|@class="subject common"]/span/@id')
        list_id = response.xpath('//tbody/tr/th[contains(@class, "subject")]/span/@id')
        #print "list_id = ", list_id 
        link_lists_url = []
        datainfo_list = []
        for id in list_id:
            # 获取tbody的id
            id = id.extract().replace("thread", "normalthread")
            # 获取被顶次数的list
            link_lists_ding = response.xpath('//tbody[@id="%s"]/tr/th/font'%id)
            if [] == link_lists_ding:
                continue 
            # 获取被顶次数（纯数字）
            int_beiding = re.search(r"\d+", link_lists_ding.extract()[0])
            # 被顶次数大于100的才去获取链接
            if int(int_beiding.group()) > 200:
                #print "int_beiding = ", int_beiding.group()
                # 获取帖子链接
                link_lists_url_temp = response.xpath('//tbody[@id="%s"]/tr/th/span/a/@href'%id)
                linkname = response.xpath('//tbody[@id="%s"]/tr/th/span/a/text()'%id).extract()[0]
                page = response.xpath("//div/strong/text()").extract()[0]
                url = "http://93.t9p.today/" + link_lists_url_temp.extract()[0].split("&page")[0]
                datainfo = linkname + ",被顶" + int_beiding.group() + "次," + "第" + page + "页," + "url = " + url + '\n'

                yield scrapy.Request(url,meta={'datainfo':datainfo}, callback = self.parse_sickinfo)

                # 帖子链接加入link_lists_url列表中
                #link_lists_url.append(link_lists_url_temp.extract()[0].split("&page")[0])
                #datainfo_list.append(datainfo)

        # 链接去重
        #link_lists_url = set(link_lists_url)
        #datainfo_list = set(datainfo_list)

        # 组合成完整的链接
        #for sub_url,datainfo in zip(link_lists_url, datainfo_list):
            #url = "http://93.t9p.today/" + sub_url
            #print "datainfo = ", datainfo
            #print "url = ", url 
            #yield scrapy.Request(url,meta={'datainfo':datainfo+url.encode("utf-8")+'\n'}, callback = self.parse_sickinfo)


    def parse_sickinfo(self, response):
        # 帖子名称(标题)
        roomname = response.xpath('//div/h1/text()').extract()[0]
        # 图片名称(哈希值)列表
        list_filename = re.findall(r'[^<a.*?]<img\ssrc=".*?"\sfile="(.*?)"', response.body)
        datainfo = response.meta["datainfo"]
        for src in list_filename:
            # 组合成完整的链接
            fullsrc = "http://93.t9p.today/" + src
            yield scrapy.Request(fullsrc, meta={'roomname':roomname, "datainfo":datainfo},callback = self.parse_image)

    def parse_image(self, response):
        item = Spider91PornItem()
        # 帖子名(标题)
        item["roomname"] = response.meta["roomname"]

        #print 'item["roomname"] = ', item["roomname"]

        # 图片链接
        item["name"] = response.url

        # 帖子信息(帖子名称，帖子链接，帖子被顶次数)
        item["datainfo"] = response.meta["datainfo"]

        #print 'item["datainfo"] = ', item["datainfo"]
        #print "item['name'] = ", item["name"]

        # 图片数据
        item["image"] = response.body 

        # 将数据传给管道文件进行处理
        yield item
