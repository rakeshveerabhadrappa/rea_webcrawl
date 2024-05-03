# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:33:38 2024

@author: Backpack1
"""

from bs4 import BeautifulSoup
import requests
import scrapy
from scrapy.http import HtmlResponse

headers ={
  "Accept-Ranges bytes": "Content-Type text/html",
  "ETag \"7360b373655b812806b66a16df48bb481462085440\"": "Last-Modified Sun, 01 May 2016 065040 GMT",
  "Server AkamaiNetStorage": "Vary Accept-Encoding",
  "Content-Encoding gzip": "Expires Mon, 29 Jan 2024 073247 GMT",
  "Cache-Control max-age=0, no-cache, no-store": "Pragma no-cache",
  "Date Mon, 29 Jan 2024 073247 GMT": "Content-Length 20",
  "Connection keep-alive": "Set-Cookie reauid=5dc7ce1702a525009f54b765d5020000979b0100; expires=Mon, 31-Dec-2038 235959 GMT; path=/; domain=.realestate.com.au, Country=AU; path=/; domain=.realestate.com.au"
}
url = 'https://www.realestate.com.au/buy/list-1?activeSort=list-date'
response = requests.get(url, headers = headers)


if response.status_code == 200:
    filename = 'webpage_source.txt'
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    property_price = soup.select_one('span.property-price').get_text(strip=True)
    print(property_price)
    
    # Create a response object
    response_scrapy = HtmlResponse(url=url, body=response.text, encoding='utf-8')
    
    address = response_scrapy.css('h2.residential-card__address-heading span::text').extract()
    price = response_scrapy.css('span.property-price ::text').extract()
    beds = response_scrapy.css('div.View__PropertyDetail-sc-11ysrk6-0:nth-child(1) p.Text__Typography-sc-vzn7fr-0::text').extract()
    baths = response_scrapy.css('div.View__PropertyDetail-sc-11ysrk6-0:nth-child(2) p.Text__Typography-sc-vzn7fr-0::text').extract()

    
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")