# -*- coding: utf-8 -*-

# Scrapy settings for xinli project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xinli'

SPIDER_MODULES = ['xinli.spiders']
NEWSPIDER_MODULE = 'xinli.spiders'
RETRY_ENABLED = True
RETRY_TIMES = 10
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'xinli (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
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
DEFAULT_REQUEST_HEADERS = {
    'Cookie':'log_session_id=eyJpdiI6IjlOek9yeDdDbUlXNGxhWGRKXC9oTHZBPT0iLCJ2YWx1ZSI6Im9LSVpIVmJXeVFheFZ4T2o4d1dENzBLUkxERjhxWXFyTUtjZUJUS3pjdG89IiwibWFjIjoiNzkzNTNiMDU4MjhmODQxMTBmMTE3NGQ5ZDQ3N2M5MTdmZmMyMWQ5MTdlODk5OGMzODVjYTI5MmJiMDliYzkzNiJ9; zg_be2579193b754fd2900f660a0093fa62=%7B%22sid%22%3A%201500560602.43%2C%22updated%22%3A%201500560612.041%2C%22info%22%3A%201500560602433%7D; zg_did=%7B%22did%22%3A%20%2215d6059b64510-0bf2c04364ed36-6555772d-1fa400-15d6059b646bd6%22%7D; zg_18f5038ab49c4ae4918641ae36d67496=%7B%22sid%22%3A%201500560078.409%2C%22updated%22%3A%201500560727.402%2C%22info%22%3A%201500560078411%7D; _ga=GA1.2.180658261.1500560078; _gid=GA1.2.1603525330.1500560078; Hm_lvt_d64469e9d7bdbf03af6f074dffe7f9b5=1500560079; Hm_lpvt_d64469e9d7bdbf03af6f074dffe7f9b5=1500560728; laravel_session=eyJpdiI6InJIWndiekJXaGdScHBXQXRmazduenc9PSIsInZhbHVlIjoiRWhLRXU2NU5UcHJXbzMrTzVKdEcwVE5vbmJpT2UwK0t3SnJWd1o3SDcycjhabWNKeCtSYTdrYThVWXE4XC92NHJPamR6bkIycmtXYlpwZlBwTllzT2NRPT0iLCJtYWMiOiI0YTNiOGEyZGNhZjJkZDIyZDZmMzQyOTc3NTFhOGY5NDNjZmM2ZDg0YjM5ZmYwMGViN2Y0ZjNhMmU1ODhkZGJiIn0%3D',
    'Host':'fm.xinli001.com',
    'Upgrade-Insecure-Requests':1,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3141.7 Safari/537.36'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'xinli.middlewares.XinliSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'xinli.middlewares.XinliMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'xinli.pipelines.XinliPipeline': 300,
   'xinli.pipelines.XinliToRedisPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
