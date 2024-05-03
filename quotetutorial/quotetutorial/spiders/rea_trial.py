# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:23:43 2024

@author: Backpack1
"""

import scrapy



class RealEstateSpider(scrapy.Spider):
    name = 'real_estate'
    allowed_domains = ['www.realestate.com.au']
    

    cookies = {
    'reauid': '547662688c4100005bfcc662d802000027a00900',
    'Country': 'US',
    'split_audience': 'e',
    'fullstory_audience_split': 'B',
    'pageview_counter.srs': '3',
    'AMCV_341225BE55BBF7E17F000101%40AdobeOrg': '-330454231%7CMCIDTS%7C19181%7CMCMID%7C40562913130153436483026945851729928270%7CMCAID%7CNONE%7CMCOPTOUT-1657305978s%7CNONE%7CMCAAMLH-1657903578%7C9%7CMCAAMB-1657903578%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19188%7CvVersion%7C3.1.2',
    '_sp_id.2fe7': 'f04532c6-7eff-4510-9f46-a1637b4f9d9e.1657207905.2.1657298780.1657207922.ca64a257-4df2-4c86-836b-ee84f7623444',
    'mid': '16329776161705650988',
    '_gcl_au': '1.1.1838423196.1657207906',
    '_ga_F962Q8PWJ0': 'GS1.1.1657298779.3.1.1657298779.0',
    '_ga': 'GA1.3.122498511.1657207906',
    'DM_SitId1464': 'true',
    'DM_SitId1464SecId12708': 'true',
    's_ecid': 'MCMID%7C40562913130153436483026945851729928270',
    'AMCVS_341225BE55BBF7E17F000101%40AdobeOrg': '1',
    'External': '%2FAPPNEXUS%3D0%2FCASALE%3D0%2FOPENX%3D1c46c6ca-49f7-4e85-8e53-df51c5836f63%2FPUBMATIC%3D164D9B19-CF60-4BBC-967B-99F765370BA2%2FRUBICON%3DL5B6SW92-N-17X3%2FTRIPLELIFT%3D106805729842281714002%2F_EXP%3D1688834837%2F_exp%3D1688834838',
    'VT_LANG': 'language%3Den-US',
    'QSI_HistorySession': 'https%3A%2F%2Fwww.realestate.com.au%2Fsold%2Fin-brisbane%2B-%2Bgreater%2Bregion%2C%2Bqld%2Flist-1~1657207910104',
    'nol_fpid': '4ajjr7ztynccd67dremidougkq4761657207910|1657207910320|1657207926812|1657207927050',
    'cto_bundle': 'nLopul8lMkZndkdvTnFkOGEzSWdDbWZiTGdiYUtVJTJCb1lHUWM1RjdIJTJCTG9nWExBQzRPYzdJWjVTVnBoRmx0eU5zTzIlMkZjVXFIdXVaYUpjM3lONXFBU0Ezd3hiRWo3N0FaZWlZQ2lNS0NDbkpuNUNLcktNSHhVZnJBRkd3ZXluQ1ZiZWNXc0wyaGZnRlp3dGlhZWwlMkZMSGc4bUVxRjJnJTNEJTNE',
    '_fbp': 'fb.2.1657207911199.715859527',
    'QSI_SI_eUTxcS7Ex4BwMYt_intercept': 'true',
    'KP2_UIDz-ssn': '07zhEGcjTRPiwRZzYptXMg0Ec0xmc8b0h4liOLtc9xwkA86wmGHH0Gn9ee3rCatQ4nQ5wxZDfMr42anMhx6OiNSR2KkpJLTdDmofxTCS4KpuD9vdVZ3piWCctOREJyzGQSWDBMeXK8LWFtMbVEFRdpNcZOcgUzT98rHKUMAUXWro4x3bWjm7LdLMU4l',
    'KP2_UIDz': '07zhEGcjTRPiwRZzYptXMg0Ec0xmc8b0h4liOLtc9xwkA86wmGHH0Gn9ee3rCatQ4nQ5wxZDfMr42anMhx6OiNSR2KkpJLTdDmofxTCS4KpuD9vdVZ3piWCctOREJyzGQSWDBMeXK8LWFtMbVEFRdpNcZOcgUzT98rHKUMAUXWro4x3bWjm7LdLMU4l',
    '_sp_ses.2fe7': '*',
    'DM_SitIdT1464': 'true',
    'DM_SitId1464SecIdT12708': 'true',
    '_gid': 'GA1.3.437462869.1657298782',
    }

    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'If-None-Match': 'W/"101189-/8ueETLeJ0u2liUpilB9lkVxr6w"',
    'Cache-Control': 'max-age=0',
    }

    def start_requests( self ):
        yield scrapy.Request('https://www.realestate.com.au/buy/list-1?activeSort=list-date', headers= self.headers, cookies=self.cookies)

    def parse(self, response):
        link_property = response.css('span.property-price ::text').get()
        print(link_property)