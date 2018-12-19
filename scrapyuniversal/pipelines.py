# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.utils.project import get_project_settings
class ScrapyuniversalPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_DBNAME']
        sheetname = settings['MONGODB_SHEETNAME']
        client = pymongo.MongoClient(host = host,port = port)
        mydb = client[dbname]
        self.post = mydb[sheetname]

    def process_item(self,item,spider):
    	data = dict(item)
    	self.post.insert(data)
    	return item
