import scrapy
from music_Spider.items import scoreSpiderItem
from scrapy.linkextractors import LinkExtractor
import re

class Music_spider(scrapy.Spider):
    
    name = 'music_spiders'
    
    start_urls = ['http://rsj.beijing.gov.cn/integralpublic/settlePerson/tablePage']

    def parse(self, response):
        for i in range(1,62):
            yield scrapy.FormRequest('http://rsj.beijing.gov.cn/integralpublic/settlePerson/tablePage',formdata = {'name':'','rows':'100','page':str((i-1)*100)},callback=self.page_parse)
    def page_parse(self,response):
        datas = response.xpath('//table[@class="blue_table1"]/tbody/tr/td').extract()
        i = 0
        while i < len(datas)//5:
            item = scoreSpiderItem()
            item["seq"] = int(re.search('\">(.*)</td',datas[i*5]).group(1))
            item["name"] = re.search('\">(.*)</td',datas[i*5+1]).group(1)
            item["birth"] = re.search('\">(.*)</td',datas[i*5+2]).group(1)
            item["company"] = re.search('\">(.*)</td',datas[i*5+3]).group(1)
            item["score"] = re.search('\">(.*)</td',datas[i*5+4]).group(1)
            i+=1
            yield item
