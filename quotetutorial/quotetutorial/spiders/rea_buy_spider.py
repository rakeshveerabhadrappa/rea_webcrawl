# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:53:50 2024

@author: Rakesh
"""

import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'rea_buy'
    start_urls = ['https://www.realestate.com.au/buy/list-1']#['https://www.realestate.com.au/']
    
    def parse(self, response):
        title = response.css('title::text').extract()
        yield {'titletext':title}