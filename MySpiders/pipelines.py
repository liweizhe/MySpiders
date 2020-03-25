# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from MySpiders.libs.mock_headers import MockHeaders
import requests
from pymongo import MongoClient
import json
from MySpiders.settings import HOST, HOST_HTTPS


class MySpidersPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'company_spider':
            # print('-' * 30, 'pipeline started!', '-' * 30)
            if item.get('email'):
                self.process_email(item=item)
            if item.get('logo'):
                self.process_logo(item=item)
            # print('-' * 30, 'pipeline stopped!', '-' * 30)
        return item

    def process_email(self, item):
        headers = MockHeaders()
        headers = headers.get_headers(HOST)
        r = requests.get(url=HOST_HTTPS + item['email'], headers=headers, timeout=1000)
        dict_str = r.content.decode('utf-8')
        result_dict = json.loads(dict_str)
        item['email'] = result_dict.get('Message')

    def process_logo(self, item):
        r = requests.get(url=HOST_HTTPS + item['logo'], timeout=1000)
        item['logo'] = r.content


class MySQLPipeline(object):
    def __init__(self):
        pass


class MongoDBPipeline(object):

    def __init__(self):
        connection = MongoClient('localhost', 27017)
        db = connection['xmrc']
        self.company_collection = db['company']
        self.job_collection = db['job']

    def process_item(self, item, spider):
        item = dict(item)
        if spider.name == 'job_spider':
            self.job_collection.insert(item)
        elif spider.name == 'company_spider':
            self.company_collection.insert(item)
        return item
