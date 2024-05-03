import scrapy
import json

class MySpider(scrapy.Spider):
    name = 'get_head_cookies'
    start_urls = ['https://realestate.com.au']

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://www.realestate.com.au',
            # Add any other headers you need
        }

        cookies = {
            'cookie_name': 'cookie_value',
            # Add any other cookies you need
        }

        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers, cookies=cookies, callback=self.parse)

    def parse(self, response):
        # Your parsing logic here

        # Extracting headers and cookies from the response
        headers = response.request.headers
        cookies = response.request.cookies

        # Save headers to a JSON file
        with open('headers.json', 'w') as headers_file:
            json.dump(dict(headers), headers_file, indent=2)
            self.log('Headers saved to headers.json')

        # Save cookies to a JSON file
        with open('cookies.json', 'w') as cookies_file:
            json.dump(cookies, cookies_file, indent=2)
            self.log('Cookies saved to cookies.json')
