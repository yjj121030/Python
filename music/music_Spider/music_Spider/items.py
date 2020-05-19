# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class scoreSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    
    # 序号
    seq = scrapy.Field()
    
    # 姓名
    name = scrapy.Field()

    # 出生年月
    birth = scrapy.Field()

    #单位名称
    company = scrapy.Field()

    # 积分分值
    score = scrapy.Field()