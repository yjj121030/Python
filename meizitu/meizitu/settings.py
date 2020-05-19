# -*- coding: utf-8 -*-

# Scrapy settings for meizitu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'meizitu'

SPIDER_MODULES = ['meizitu.spiders']
NEWSPIDER_MODULE = 'meizitu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'meizitu (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
DEFAULT_REQUEST_HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0',
    'Referer':'https://www.mzitu.com/xinggan/',
    'Cookie':'BAIDUID=F660214629B549A8C8C22F50416150B7:FG=1; BIDUPSID=F660214629B549A8C8C22F50416150B7; PSTM=1540432706; HMACCOUNT=03EE5D782043D96A; BDUSS=X4teUpSZGxxVUNwZmNuaEFzfnFsazlDYjFFSjRGY3ZMMXpMRHF3ZnRlOVVFdmxiQVFBQUFBJCQAAAAAAAAAAAEAAACwLQs30Ka~tMLkyNWy0NH0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFSF0VtUhdFbU; H_PS_PSSID=1447_21125_20697_28557_28608_28584_28604_28626_28605; HMVT=6bcd52f51e9b3dce32bec4a3997715ac|1552549118|dbc355aef238b6c32b43eacbbf161c3c|1552549160|; delPer=0; PSINO=1; BDRCVFR[gltLrB7qNCt]=mk3SLVN4HKm; cflag=13%3A3; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BDRCVFR[SsB3xVCBoFf]=Ae1_MfEv1LYmLPbUB48ugf; locale=zh'
}
IMAGES_STORE = 'meizitudownload'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'meizitu.middlewares.MeizituSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'meizitu.middlewares.MeizituDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'meizitu.pipelines.MeizituPipeline': 300,
#}
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline':1,
}
#DOWNLOAD_DELAY = 3
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
