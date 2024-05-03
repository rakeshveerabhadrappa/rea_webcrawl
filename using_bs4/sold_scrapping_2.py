# -*- coding: utf-8 -*-
"""
Vic 3024 Manor Lakes
sold data
1. search based on sortdate
2. include nearby suburbs is set to false
"""

from bs4 import BeautifulSoup
import requests
import re
from tqdm import tqdm
import time
from utils import read_header

headers ={
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "en-US,en;q=0.9",
  "Cache-Control": "max-age=0",
  "Cookie": "External=%2FTRIPLELIFT%3D4179063217492860574542%2F_EXP%3D1727492884%2F_exp%3D1728132166; reauid=6f58d617c29f1d00a2f0b465fe010000dd920f00; split_audience=e; mid=830284722336911708; VT_LANG=language%3Den-US; s_ecid=MCMID%7C00081940520873696161441832336372005742; _fbp=fb.2.1706356899232.1418471802; _gcl_au=1.1.1462191025.1706356899; _gid=GA1.3.1276459289.1706479868; KP_UIDz-ssn=0p6Yz2QINcIpPyNAZR8cumMiaeBPkKzKEzOU7m3cxW33evU02O70Oha7fSDu7lCXVf6uMPmYNPrI0060Kux1IQywXJQFF1Fnu8AxolIqZutbCpcG0Ur1ICTZp7xDkr2qbxnuKTR4LDEek9prfYmKaoQ8mdnH; KP_UIDz=0p6Yz2QINcIpPyNAZR8cumMiaeBPkKzKEzOU7m3cxW33evU02O70Oha7fSDu7lCXVf6uMPmYNPrI0060Kux1IQywXJQFF1Fnu8AxolIqZutbCpcG0Ur1ICTZp7xDkr2qbxnuKTR4LDEek9prfYmKaoQ8mdnH; topid=REAUID6F58D617C29F1D00A2F0B465FE010000DD920F00; Country=AU; fullstory_audience_split=A; _sp_ses.2fe7=*; AMCVS_341225BE55BBF7E17F000101%40AdobeOrg=1; AMCV_341225BE55BBF7E17F000101%40AdobeOrg=-330454231%7CMCIDTS%7C19752%7CMCMID%7C00081940520873696161441832336372005742%7CMCAID%7CNONE%7CMCOPTOUT-1706519988s%7CNONE%7CMCAAMLH-1707117588%7C8%7CMCAAMB-1707117588%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19757%7CvVersion%7C3.1.2; s_cc=true; ab.storage.deviceId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%229d9801e2-d848-b74d-c7e4-2104ddbcdb84%22%2C%22c%22%3A1706356898990%2C%22l%22%3A1706512788158%7D; ab.storage.userId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%22cbf90abc-23ff-4f15-9148-9c30154043c9%22%2C%22c%22%3A1706356898986%2C%22l%22%3A1706512788159%7D; DM_SitId1464=1; DM_SitId1464SecId12707=1; _gat_gtag_UA_143679184_2=1; s_nr30=1706512789242-Repeat; s_sq=%5B%5BB%5D%5D; _sp_id.2fe7=f5ce7e77-ff9f-40aa-a8ea-d4c5241f531a.1688111822.70.1706512789.1706480276.69c7a929-6a89-49c5-b2f7-e5b3b9b2a990; utag_main=v_id018d4acbfb3c004fec638b1b8ca80507d005407500bd0$_sn3$_se2$_ss0$_st1706514589108$vapi_domainrealestate.com.au$dc_visit3$ses_id1706512787768%3Bexp-session$_pn2%3Bexp-session$_prevpagerea%3Asold%3Ahomepage%3Bexp-1706516389241$dc_event2%3Bexp-session$dc_regionap-southeast-2%3Bexp-session; ab.storage.sessionId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%22992c3bde-2815-2e34-1625-0d4edc8a33c5%22%2C%22e%22%3A1706514589352%2C%22c%22%3A1706512788158%2C%22l%22%3A1706512789352%7D; _ga_F962Q8PWJ0=GS1.1.1706512788.3.1.1706512789.0.0.0; _ga_3J0XCBB972=GS1.1.1706512788.3.1.1706512789.0.0.0; _ga=GA1.3.687049223.1706356900; nol_fpid=un3xkitlz8nysegxtzy8zmhgsp18z1706356899|1706356899426|1706512789459|1706512789476; DM_SitId1464SecId12708=1; QSI_HistorySession=https%3A%2F%2Fwww.realestate.com.au%2Fsold%2F~1706512789599",
  "Referer": "https//www.realestate.com.au/",
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

url = f'https://www.realestate.com.au/sold/in-{suburb},+{state}+{pc}/list-1?includeSurrounding=false&activeSort=solddate&source=refinement'
response = requests.get(url, headers = headers)

n_pages = get_n_pages(response)
data = []
data = start_scrapping(response, data)

for n_page in tqdm(range(2,n_pages+1)):
    url = f'https://www.realestate.com.au/sold/in-{suburb},+{state}+{pc}/list-{n_page}?includeSurrounding=false&activeSort=solddate&source=refinement'
    response = requests.get(url, headers = headers)
    data = start_scrapping(response, data)
#%%
import pandas as pd
data_df= pd.DataFrame(data)
data_df.to_csv(f'../data/Sold/sold_{suburb}_{state}_{pc}.csv', index = False)
#%%
