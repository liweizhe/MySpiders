# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspidersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CompanyItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    contact = scrapy.Field()
    info = scrapy.Field()
    Tel = scrapy.Field()
    address = scrapy.Field()
    nature = scrapy.Field()
    industry = scrapy.Field()
    scale = scrapy.Field()
    email = scrapy.Field()
    logo = scrapy.Field()
    job = scrapy.Field()


class JobItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    company = scrapy.Field()
    time = scrapy.Field()
    department = scrapy.Field()
    contact = scrapy.Field()
    Tel = scrapy.Field()
    address = scrapy.Field()
    education = scrapy.Field()
    nature = scrapy.Field()
    experience = scrapy.Field()
    age = scrapy.Field()
    location = scrapy.Field()
    salary = scrapy.Field()
    schedule = scrapy.Field()
    welfare = scrapy.Field()
    response_and_require = scrapy.Field()
