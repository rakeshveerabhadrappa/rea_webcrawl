# -*- coding: utf-8 -*-
"""
Vic 3024 Manor Lakes
sold data
"""

from bs4 import BeautifulSoup
import requests
import re
from tqdm import tqdm
import time

headers ={
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "en-US,en;q=0.9",
  "Cache-Control": "max-age=0",
  "Cookie": "External=%2FTRIPLELIFT%3D4179063217492860574542%2F_EXP%3D1727492884%2F_exp%3D1728132166; reauid=6f58d617c29f1d00a2f0b465fe010000dd920f00; Country=AU; KP_UIDz-ssn=0qzOS6ZyXteB3eCT775CxGTF9p2HOOVCgBpC5Z4IlxMzL4VeW6jFMIrgP4k89w9JmjLiVXXZuxaxE6WDvt1vcUy9FP2gpz94zwmw2gyeIKdPYLUH58jyKMzWFH6S9SYeDRIluJzCzKwn8gUaaJNGbQuoN90B; KP_UIDz=0qzOS6ZyXteB3eCT775CxGTF9p2HOOVCgBpC5Z4IlxMzL4VeW6jFMIrgP4k89w9JmjLiVXXZuxaxE6WDvt1vcUy9FP2gpz94zwmw2gyeIKdPYLUH58jyKMzWFH6S9SYeDRIluJzCzKwn8gUaaJNGbQuoN90B; split_audience=e; fullstory_audience_split=B; pageview_counter.srs=1; mid=830284722336911708; VT_LANG=language%3Den-US; _sp_ses.2fe7=*; s_ecid=MCMID%7C00081940520873696161441832336372005742; s_nr30=1706356898957-New; AMCVS_341225BE55BBF7E17F000101%40AdobeOrg=1; ab.storage.userId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%22cbf90abc-23ff-4f15-9148-9c30154043c9%22%2C%22c%22%3A1706356898986%2C%22l%22%3A1706356898988%7D; ab.storage.deviceId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%229d9801e2-d848-b74d-c7e4-2104ddbcdb84%22%2C%22c%22%3A1706356898990%2C%22l%22%3A1706356898990%7D; s_cc=true; _fbp=fb.2.1706356899232.1418471802; DM_SitId1464=1; DM_SitId1464SecId12708=1; nol_fpid=un3xkitlz8nysegxtzy8zmhgsp18z1706356899|1706356899426|1706356899426|1706356899426; _gcl_au=1.1.1462191025.1706356899; _gid=GA1.3.1695040248.1706356900; _gat_gtag_UA_143679184_2=1; _ga_F962Q8PWJ0=GS1.1.1706356899.1.0.1706356899.0.0.0; _ga=GA1.1.687049223.1706356900; _ga_3J0XCBB972=GS1.1.1706356899.1.0.1706356899.0.0.0; AMCV_341225BE55BBF7E17F000101%40AdobeOrg=-330454231%7CMCIDTS%7C19750%7CMCMID%7C00081940520873696161441832336372005742%7CMCAID%7CNONE%7CMCOPTOUT-1706364098s%7CNONE%7CMCAAMLH-1706961699%7C8%7CMCAAMB-1706961699%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19757%7CvVersion%7C3.1.2; _lr_geo_location_state=VIC; _lr_geo_location=AU; reaidtok=eyJ1aWQiOiI0MDI4N2YwYTY5MDg0OWU3MDE2OTE5NmU0YzEzMGY5YiIsImVtYWlsVmVyaWZpZWQiOnRydWUsImV4cGlyeU1pbGxzIjoxNzA2MzU3ODAxMTI0fQ==.GMWg2lQpcP2wmCvx+odE2+qgIvIssBKG9jQT7OI+JZYJsYeTEDzmWpkJ/EXUzEjA; reastok=NDAyODdmMGE2OTA4NDllNzAxNjkxOTZlNGMxMzBmOWI6MTcwNjM1NzgwMTEyNDpQa1ZDcjhkYkJwc2R6bnJPejl1TndHajJBeXpCSUFJclFueTJhTTAvT3VMajNpNEJyeGh2RUVSUzFPaWxmeGlq; reautok=eyJraWQiOiI1ODQzNzNlMy0xMjUxLTExZWEtYWQ3Yi00ZTAwYWMyYTA1MDUiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibGlkIjoiY2JmOTBhYmMtMjNmZi00ZjE1LTkxNDgtOWMzMDE1NDA0M2M5IiwiaXNzIjoiaHR0cHM6XC9cL3d3dy5yZWFsZXN0YXRlLmNvbS5hdSIsIm1mYV9lbmFibGVkIjpmYWxzZSwiZXhwIjoxNzA2MzU3ODAxLCJpYXQiOjE3MDYzNTY5MDEsImVtYWlsIjoicmFraS5jaG93bHVyQGdtYWlsLmNvbSIsImp0aSI6InY4OUZHZWZoWWR4WFdvZkZMVElZZUFxcmJNcz0iLCJjaWQiOiI0MDI4N2YwYTY5MDg0OWU3MDE2OTE5NmU0YzEzMGY5YiJ9.ItbzthbUNrgy9ZxImfXNg-c_EEW-G-8cEtsa4EIAAprbzfsF3GjpcI7ZiEI3RGThAGRPDs_3CPPBd9I_YzkWQ0TAjjulDOa37yA29Q4emHokulriJZpIPfi8AD0Y4suRDUGNydlQfruDHdgNZVGYy0ItzfhL4U7esVLcSnI9v6i2LoNPaG8-PO3gseal6FyYAmeeYABh1uHvk9hVqHD1BahNTZaj4L6B9rElf8mozrFs1bN2VQfB5Wm3ebGLZDxhZrv7Jq3di4F8F3RAGZgBnCPZlCqFTbbHG4gcij2TRW92Gro_kA7QCNEAik5WgThebFKjACruu4w7yqYEVez_KQ; reauinf=eyJtbGlkIjoicmEqKipyQGdtKioqLmNvbSIsImdlaWQiOiI4ZDcyN2E3OTE2YmEyNzU5ODRjNGY5YmU1NzQwMWQ5MDFiYmRjYTg5NjJjZDkxYjIwOTM2YTU4ZWU1YmFhYzI2IiwiY2lkIjoiNDAyODdmMGE2OTA4NDllNzAxNjkxOTZlNGMxMzBmOWIiLCJsaWQiOiJjYmY5MGFiYy0yM2ZmLTRmMTUtOTE0OC05YzMwMTU0MDQzYzkiLCJpc05ld1VzZXIiOmZhbHNlLCJleHBpcnlNaWxsaXMiOjE3Mzc4OTI5MDExMjl9; QSI_HistorySession=https%3A%2F%2Fwww.realestate.com.au%2Fsold%2Fin-manor%2Blakes%2C%2Bvic%2B3024%2Flist-1%3Fsource%3Drefinement~1706356901712; myid5_id=ID5*vDuvy-GUcK94dgZhV44SMBKaQ3UGywZhV44SMBKaQ3V_qqGpiCY-4bMha_6AcRPPf6s8Khrz3vyN4N3K3-lYmw; utag_main=v_id018d4acbfb3c004fec638b1b8ca80507d005407500bd0$_sn1$_se3$_ss0$_st1706358704021$ses_id1706356898620%3Bexp-session$_pn1%3Bexp-session$vapi_domainrealestate.com.au$dc_visit1$dc_event1%3Bexp-session$dc_regionap-southeast-2%3Bexp-session$_prevpagerea%3Asold%3Asearch%20result%20-%20list%3Bexp-1706360504025$ttd_uuid7af6af98-57ec-4a8c-b3a5-0c5e0bc670be%3Bexp-session; _sp_id.2fe7=f5ce7e77-ff9f-40aa-a8ea-d4c5241f531a.1688111822.68.1706356904.1695510962.7178cce5-4474-4cc7-a885-03b1f8899dc0; ab.storage.sessionId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%22a94b7ec4-fec0-f915-8fb8-01b0e32d1124%22%2C%22e%22%3A1706358704039%2C%22c%22%3A1706356898987%2C%22l%22%3A1706356904039%7D",
  "Referer": "https//www.realestate.com.au/sold/in-manor+lakes,+vic+3024/list-1?source=refinement",
  "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Microsoft Edge\";v=\"121\", \"Chromium\";v=\"121\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Windows\"",
  "Sec-Fetch-Dest": "document",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-Site": "same-origin",
  "Sec-Fetch-User": "?1",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
}

suburb = "manor+lakes"
state = "vic"
pc = "3024"
#%%
def get_n_pages(_response):
    if _response.status_code == 200:
        
        soup = BeautifulSoup(_response.text, "lxml")
        
        page_elements = soup.findAll('div', {'class': 'styles__PaginationNumbers-sc-1ciwyuo-5 cTcyaO'})
        lastPageData = page_elements[0].find_all('a', {'aria-label': True})[-1]
        n_pages = re.sub(r'\D', '',lastPageData['aria-label'] )  
    else:
        print(f"Failed to fetch the page. Status code: {_response.status_code}, REGENERATE HEADER")
    
    return int(n_pages)

def get_agency_agent(div):
    try:
        agency = div.find("img", {'class': "branding__image"}).get('alt')
    except Exception as e:
        agency = 'N/A'
       
    try:
        agent = div.find("p", {'class': "agent__name"}).get_text(strip=True)
        # remove "Agent: "
        agent = agent.strip("Agent: ")
        agent = agent.lstrip()
    except Exception as e:
        agent = 'N/A'

    
    return agency, agent

def get_sell_date(residential_content):
    try:
        date = residential_content.findAll('span')[-1].get_text()
    except Exception as e:
        date = 'N/A'
    return date.strip("Sold on")


def get_features(_residential_content,_address_text):
    houseOrLand = _residential_content.find('h2', class_='residential-card__address-heading').find_next('a').get('href')
    
    # only do this process if property type is House     
    beds = 'N/A'
    baths = 'N/A'
    park = 'N/A'
    land_size = 'N/A'
    if (("house" in houseOrLand) and ("land" not in houseOrLand)):
        property_details_div = _residential_content.find('div', {'class': 'Inline__InlineContainer-sc-lf7x8d-0 iuOPWU'})
    
    
        details_elements= None
        try:
            details_elements = property_details_div.find_all('div', {'class': 'View__PropertyDetail-sc-11ysrk6-0 eSRWKr'})
        except Exception as e:
            print(f'no features information available for {_address_text}')
            pass
        
        details = {}      
        
        if details_elements is not None:
            for detail_element in details_elements:
                icon_type = detail_element.find('svg').find('use')['href'].replace('#ck-sprite-', '')
                try:
                    value = detail_element.find('p').get_text(strip=True)
                except Exception as e:
                    continue
                details[icon_type] = value
            
    
            # Access the values using the icon types
            beds = details.get('beds', 'N/A')
            baths = details.get('baths', 'N/A')
            park = details.get('cars', 'N/A')
    
    try:
        land_size = property_details_div.find('div', {'class': 'View__PropertySize-sc-1psmy31-0 iATXcS property-size'}).find('div').get_text(strip=True)
    except Exception as e:
        pass
    
    return beds, baths, park, land_size, houseOrLand
    

def start_scrapping(_response, data):
    
    if _response.status_code == 200:
        
        soup = BeautifulSoup(_response.text, "lxml")               
        
        presentation_divs = soup.findAll("div", {'class': "", 'data-testid':"", 'role': 'presentation'})
        for div in presentation_divs:
            
            agency, agent = get_agency_agent(div)
            
            residential_content = div.find('div', {'class': 'residential-card__content', 'role': 'presentation'})
            sold_on = get_sell_date(residential_content)
            
            
            if residential_content is None:
                continue

            try:
                property_price_span = residential_content.find('span', {'class': 'property-price'})
                property_price = property_price_span.get_text(strip=True)
            except Exception as e:
                property_price = 'N/A'

            address_text = residential_content.find('h2', class_='residential-card__address-heading').get_text()        
            
    
            # Extract the number of bedrooms, bathrooms, and parking spaces
            beds, baths, park, land_size, p_type = get_features(residential_content, address_text)
                

            # Extract house property type and land size

            property_type = residential_content.find('span', {'class': 'residential-card__property-type'}).get_text(strip=True)
            
            
            data.append({'sold_on':sold_on,
                        'price':property_price, 
                         'address': address_text, 
                         'bedrooms': beds,
                         'bathrooms':baths, 
                         'parking space': park, 
                         'land size': land_size,
                         'property type1'
                         'property type2': property_type,
                         'agency': agency,
                         'agent': agent
                         })
        
    else:
        print(f"Failed to fetch the page. Status code: {_response.status_code}")
    
    return data

#%%
url = f'https://www.realestate.com.au/sold/in-{suburb},+{state}+{pc}/list-1?source=refinement'
response = requests.get(url, headers = headers)

n_pages = get_n_pages(response)
data = []
data = start_scrapping(response, data)

for n_page in tqdm(range(2,n_pages+1)):
    url = f'https://www.realestate.com.au/sold/in-{suburb},+{state}+{pc}/list-{n_page}?source=refinement'
    response = requests.get(url, headers = headers)
    data = start_scrapping(response, data)
#%%
import pandas as pd
data_df= pd.DataFrame(data)
data_df.to_csv(f'../data/sold_{suburb}_{state}_{pc}.csv', index = False)
#%%
