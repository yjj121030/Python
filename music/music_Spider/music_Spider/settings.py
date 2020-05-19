# -*- coding: utf-8 -*-

# Scrapy settings for music_Spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'music_Spider'

SPIDER_MODULES = ['music_Spider.spiders']
NEWSPIDER_MODULE = 'music_Spider.spiders'

# DEFAULT_REQUEST_HEADERS = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36',
#     'Referer':'https://music.douban.com/',
#     'Cookie':'bid=bTPpf_SQY0A; _vwo_uuid_v2=DB58C702E8E986A195140F59158A93BDF|3ad53772e9645caf984f9f5dc6849396; __utmc=30149280; __utmz=30149280.1563332391.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.afe6=%5B%22%22%2C%22%22%2C1563345460%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DTVkFrQtVHZNGVbei2X8hDn2gOfEHQ52wLA892wb7c-aAHda5mr-1vM47Q2zqt7wp%26wd%3D%26eqid%3Df1d109bd000812a2000000035d2e8f08%22%5D; _pk_ses.100001.afe6=*; ap_v=0,6.0; viewed="2995812_1395089_1403307_1427374_3040149"; __utma=30149280.439447361.1563332391.1563332391.1563345502.2; __utmt=1; _pk_id.100001.afe6=649526fbc35d9c4d.1561779487.3.1563345515.1563332945.; __utmb=30149280.4.10.1563345502'
# }
MONGODB_URL = 'mongodb://localhost:27017/'
MONGODB_NAME = 'score'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'music_Spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'music_Spider.pipelines.MongoDBPipelines': 300,
}
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
#    'music_Spider.middlewares.MusicSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'music_Spider.middlewares.MusicSpiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html


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
