# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 16:29:02 2024

@author: Rakesh
"""

import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'rea'
    allowed_domains = ['realestate.com.au']
    start_urls = ['https://www.realestate.com.au']
    max_pages = 5 
    
    def __init__(self, *args, **kwargs):
        super(ExampleSpider, self).__init__(*args, **kwargs)
        self.page_count = 0  # Initialize the page count

    def parse(self, response):
        # Extract data from the page
        title = response.css('title::text').get()
        body = response.css('body::text').get()

        # Print the extracted data
        self.log(f'Title: {title}')
        self.log(f'Body: {body}')
        
        # Increment the page count
        self.page_count += 1
        
        # Check if the maximum page count is reached
        if self.page_count >= self.max_pages:
            self.log(f'Reached maximum page count ({self.max_pages}). Stopping the spider.')
            return

        # Follow links to other pages
        for next_page in response.css('a::attr(href)').getall():
            yield scrapy.Request(next_page, callback=self.parse)

"""
To run this scrapy type the following in the 
console

!scrapy crawl rea
"""
