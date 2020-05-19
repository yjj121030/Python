# -*- coding: utf-8 -*-
import scrapy
 
from scrapy.linkextractors import LinkExtractor 
from meizitu.items import MeizituItem
 
class MeizituSpiderSpider(scrapy.Spider):
    name = 'meizitu_spider'
    start_urls = ['https://www.mzitu.com/xinggan/']   
    def parse(self, response):
        links = response.xpath('//ul[@id="pins"]/li/a/@href').extract()
        for link in links:
            yield scrapy.Request(link,callback=self.image_parse)
        next_url = response.xpath('//a[@class="next page-numbers"]/@href').extract_first()
        if next_url:
            yield scrapy.Request(next_url,self.parse)
    def image_parse(self,response):
        next_image = response.xpath('/html/body/div[2]/div[1]/div[3]/p/a/@href').extract_first()
        iamge_url = response.xpath('/html/body/div[2]/div[1]/div[3]/p/a/img/@src').extract_first()
        item = MeizituItem()
        item['image_urls'] = [iamge_url]
        yield item
        if str(next_image).startswith(response.url[:str(response.url).rindex('/')]):
            yield scrapy.Request(next_image,self.image_parse)