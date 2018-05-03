# -*- coding: utf-8 -*-
import logging
import scrapy
from scrapy import Request
from xinli.items import XinliItem


class FmSpider(scrapy.Spider):
    name = 'fm'
    allowed_domains = ['fm.xinli001.com','ossfm.xinli001.com','yiapi.xinli001.com']
    start_url = 'http://fm.xinli001.com/broadcast-list?p={page}'
    download_base_url = 'http://yiapi.xinli001.com/fm/media-url.mp3?id={id}'

    def __init__(self):
        self.log = logging

    def start_requests(self):
        try:
            for page in range(1,10):#210
                yield Request(url=self.start_url.format(page=page), callback=self.parse)
        except ConnectionError:
            print('eee')
    def parse(self, response):
        if response.text:
            for result in response.xpath('//li'):
                item = XinliItem()
                name = result.xpath('.//div/a/text()').extract_first()
                mp3_id = result.xpath('.//div/a/@href').extract_first()
                download_url = self.download_base_url.format(id=mp3_id[1:])
                item['name'] = name
                item['download_url'] = download_url
                yield item
        else:
            self.log.debug('SYSTEM COMPLETE!')


