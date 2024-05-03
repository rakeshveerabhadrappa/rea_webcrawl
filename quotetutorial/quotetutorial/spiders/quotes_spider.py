# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:53:50 2024

@author: Rakesh
"""

import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        filename = 'webpage_source.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.body.decode('utf-8', 'ignore'))

        title = response.css('title::text').extract()
        yield {'titletext': title}
