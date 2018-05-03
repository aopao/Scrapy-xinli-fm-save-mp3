# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis
import pymongo
import requests

class XinliToRedisPipeline(object):
    # def process_item(self, item, spider):
    #     r = redis.StrictRedis('127.0.0.1',6379)
    #     r.hsetnx('down_url',item['name'],item['download_url'])
    #     r.rpush('list_url',item['download_url'])
    #     r.flushall()
    def process_item(self, item, spider):
        monogo = pymongo.MongoClient('127.0.0.1',27017)
        db = monogo.get_database('xinli')
        download = db.get_collection('download_url')
        download.insert(item)

class XinliPipeline(object):
    def process_item(self, item, spider):
        response =  requests.get(item['download_url'])
        file_name = item['name']+'.mp3'
        with open(file_name,'wb') as f:
            f.write(response.content)