# -*- coding: utf-8 -*-

BOT_NAME = 'sina'

SPIDER_MODULES = ['sina.spiders']
NEWSPIDER_MODULE = 'sina.spiders'

ROBOTSTXT_OBEY = False

# 请将Cookie替换成你自己的Cookie
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    "Cookie": "_T_WM=76476656122; SCF=Ams0FXDf5DiKh65Di8DJ_XYDJHXk0jnHsu8E6JVbhoA-STz0UfhYAGbwTOoMsA_PyZxG2TGY2WJgA9hcSWDjDG4.; SUB=_2A25w-QxfDeRhGeFN7lYY8SbPyD2IHXVQBZQXrDV6PUJbktAfLVbCkW1NQBjOhz8Fj1PvlEv0GDS7X5AEpUf5pbXb; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5uZzsE3KVunQBXWaFxNLNZ5JpX5KzhUgL.FoM0SKB4eKn0e022dJLoIEXLxKnL12-LB-zLxK-LBo5L12qLxKnLBKnL1h5LxKMLBoeL1-eLxK-L12-LBK-t; SUHB=0xnCCHmCkwxnMa; SSOLoginState=1576893455"
}

# 当前是单账号，所以下面的 CONCURRENT_REQUESTS 和 DOWNLOAD_DELAY 请不要修改

CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 3

DOWNLOADER_MIDDLEWARES = {
    'weibo.middlewares.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': None
}

ITEM_PIPELINES = {
    'sina.pipelines.MongoDBPipeline': 300,
}

# MongoDb 配置

LOCAL_MONGO_HOST = '127.0.0.1'
LOCAL_MONGO_PORT = 27017
DB_NAME = 'Sina'
