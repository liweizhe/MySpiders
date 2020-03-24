# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class MyspidersPipeline(object):
    def process_item(self, item, spider):
        return item


class MySQLPipeline(object):
    def __init__(self):
        pass
