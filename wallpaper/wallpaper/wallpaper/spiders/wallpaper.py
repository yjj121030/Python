import scrapy
from scrapy.linkextractors import LinkExtractor
from wallpaper.items import WallpaperItem
import re

class WallpaperSpider(scrapy.Spider):
    name = 'wallpaper_spider'
    #start_urls = ['http://www.win4000.com/zt/gaoqing_{0}.html'.format(i) for i in range(1,6)]
    start_urls = ['http://www.win4000.com/wallpaper_detail_162824.html']
    # def parse(self, response):
    #     le = LinkExtractor(restrict_xpaths = '/html/body/div[4]/div/div[3]/div[1]/div[1]/div[2]/div/div/ul')
    #     for link in le.extract_links(response):
    #         yield scrapy.Request(link.url,self.image_Downloader)

    # def image_Downloader(self,response):
    #     group = re.search('(\d{6})',response.request.url).group()
    #     next_image_urls = response.xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div[1]/a/@href').extract_first()
    #     image_url = response.xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div[2]/a/@href').extract_first()
    #     item = WallpaperItem()
    #     item['image_urls'] = [image_url]
    #     item['image_name'] = re.search('\d{2}/(.*\.jpg)',image_url).group(1)
    #     yield item
    #     if group in next_image_urls:
    #         yield scrapy.Request(next_image_urls,self.image_Downloader)


    def parse(self, response):
        group = re.search('(\d{6})',response.request.url).group()
        next_image_urls = response.xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[1]/div[1]/a/@href').extract_first()
        image_url = response.xpath('/html/body/div[4]/div/div[2]/div/div[1]/div[2]/div[2]/a/@href').extract_first()
        item = WallpaperItem()
        item['image_urls'] = [image_url]
        item['image_name'] = re.search('\d{2}/(.*\.jpg)',image_url).group(1)
        yield item
        if group in next_image_urls:
            yield scrapy.Request(next_image_urls,self.parse)