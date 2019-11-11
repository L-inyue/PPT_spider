# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.pipelines.files import FilesPipeline
import scrapy


class PptPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        yield scrapy.Request(
            url=item['ppt_url'],
            meta={'title': item['title']}
        )

    def file_path(self, request, response=None, info=None):
        filename = request.meta['title'] + '.zip'
        return filename
