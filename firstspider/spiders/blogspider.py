"""blog spider """
# -*- coding:utf-8 -*-
from scrapy.spiders import Spider


class BlogSpider(Spider):
    """blog spider"""
    name = 'writeathink'
    start_urls = ['http://writeathink.cn']

    def parse(self, response):
        titles = response.xpath('//a[@class="title"]').extract()
        for title in titles:
            print(title.strip())
