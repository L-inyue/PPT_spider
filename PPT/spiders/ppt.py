# -*- coding: utf-8 -*-
import scrapy
from lxml import etree
from ..items import PptItem


class PptSpider(scrapy.Spider):
    name = 'ppt'
    allowed_domains = ['www.1ppt.com']
    urls = 'http://www.1ppt.com/xiazai/huibao/ppt_huibao_{}.html'

    def start_requests(self):
        for i in range(1, 3):
            yield scrapy.Request(
                url=self.urls.format(i),
                callback=self.parse_html
            )

    def parse_html(self, response):
        html = response.text
        parse_html = etree.HTML(html)
        url_list = parse_html.xpath('//ul[@class="tplist"]/li/a/@href')
        for url in url_list:
            # http://www.1ppt.com/article/49818.html
            url = "http://www.1ppt.com" + url
            yield scrapy.Request(
                url=url,
                callback=self.parse_two_html
            )

    def parse_two_html(self, response):
        item = PptItem()
        html = response.text
        parse=etree.HTML(html)
        item['title'] = parse.xpath("//h1/text()")[0]
        # item['img_list'] = parse.xpath('//div[@class="content"]/p[1]/img/@src')
        item['ppt_url'] = parse.xpath("//ul[@class='downurllist']/li/a/@href")[0]

        # for i in img_list:
        #     yield scrapy.Request(url=i, callback=self.parse_img, meta={'title': title, 'img_url': i, 'ppt_url':ppt_url})

        yield item


    # def parse_img(self, response):
    #     item = PptItem()
    #     item['title'] = response.metap['title']
    #     item['img_url'] = response.metap['img_url']
    #     item['ppt_url'] = response.metap['ppt_url']
    #     yield item
