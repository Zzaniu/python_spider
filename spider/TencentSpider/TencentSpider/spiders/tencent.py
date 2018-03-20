# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from TencentSpider.items import TencentspiderItem


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=']

    pagelink = LinkExtractor(allow=("start=\d+"))

    rules = (
        Rule(pagelink, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentspiderItem()
            item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
            item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
            try:
                item['positiontype'] = each.xpath("./td[2]/text()").extract()[0]
            except:
                item['positiontype'] = ""

            item['peoplenum'] = each.xpath("./td[3]/text()").extract()[0]
            item['worklocation'] = each.xpath("./td[4]/text()").extract()[0]
            item['publishtime'] = each.xpath("./td[5]/text()").extract()[0]

            yield item 


        #i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        #return i
