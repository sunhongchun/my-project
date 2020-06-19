# -*- coding: utf-8 -*-
import scrapy
from stockSpider.items import StockspiderItem

# import sys
# print(sys.path)

class StockstarSpider(scrapy.Spider):
    name = 'stockStar'
    allowed_domains = ['stockstar.com']
    start_urls = ['http://quote.stockstar.com/stock/sha.shtml/']

    def parse(self, response):
        item=StockspiderItem()
        item['code']=response.xpath('//*[@id="datalist"]/tr[1]/td[1]/a/text()')

        print("code=",item['code'])
