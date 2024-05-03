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
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "en-AU,en-GB;q=0.9,en-US;q=0.8,en;q=0.7",
  "Cache-Control": "max-age=0",
  "Cookie": "mid=17645092887033873987; reauid=44c7ce175f4c0100c81e8865ac00000021f62c00; split_audience=c; s_ecid=MCMID%7C45784199353522247501280099691156033512; _gcl_au=1.1.1370370422.1703419592; VT_LANG=language%3Den-AU; _fbp=fb.2.1703419591991.1753633746; topid=REAUID44C7CE175F4C0100C81E8865AC00000021F62C00; optimizelyEndUserId=oeu1704935858292r0.22777205108329146; Country=AU; fullstory_audience_split=B; AMCVS_341225BE55BBF7E17F000101%40AdobeOrg=1; s_cc=true; DM_SitId1464=1; DM_SitId1464SecId12707=1; DM_SitId1464SecId12708=1; myid5_id=ID5*ImsMH4m-7pS6XYNjUfx2MZ03-R0e6MiQZZn-R1GT44d9ck9Ui0HK_FT5566JeIWqfXN9F4BasiP1vElpfgKMZg; External=%2FTRIPLELIFT%3D4223216941898746578742%2F_EXP%3D1737183567%2F_exp%3D1737626001; _ga_F962Q8PWJ0=deleted; QSI_HistorySession=https%3A%2F%2Fwww.realestate.com.au%2F~1706142658119%7Chttps%3A%2F%2Fwww.realestate.com.au%2Fbuy%2Flist-1%3FactiveSort%3Dprice-asc~1706142668918%7Chttps%3A%2F%2Fwww.realestate.com.au%2F~1706149354237%7Chttps%3A%2F%2Fwww.realestate.com.au%2Fbuy%2Flist-1%3FactiveSort%3Dlist-date~1706149365165%7Chttps%3A%2F%2Fwww.realestate.com.au%2F~1706154093011; _ga_F962Q8PWJ0=GS1.1.1706187620.34.1.1706187642.0.0.0; _sp_ses.2fe7=*; AMCV_341225BE55BBF7E17F000101%40AdobeOrg=-330454231%7CMCIDTS%7C19749%7CMCMID%7C45784199353522247501280099691156033512%7CMCAAMLH-1706869306%7C8%7CMCAAMB-1706869306%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1706271706s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; ab.storage.deviceId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%220b90ec51-d713-6ad4-51db-7b1a3a91c578%22%2C%22c%22%3A1703419615354%2C%22l%22%3A1706264507036%7D; ab.storage.userId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%22cbf90abc-23ff-4f15-9148-9c30154043c9%22%2C%22c%22%3A1703419615352%2C%22l%22%3A1706264507037%7D; _gid=GA1.3.1841254111.1706264508; _gat_gtag_UA_143679184_2=1; KP_UIDz-ssn=0vogLRroILuMmnh7XBNLQvgLURTputNN4aBwzTauO4n6vE3X7R8bmqbpfY6LYc85ovoaqRxyzGEVrOqSfO5w5WIyQvQJkORCmF1J5bIubNl5uhQTFxvvOCvsKHKWw2RdZ9uzzWeg1zXkEFiuoPcEOOyFAS0L; KP_UIDz=0vogLRroILuMmnh7XBNLQvgLURTputNN4aBwzTauO4n6vE3X7R8bmqbpfY6LYc85ovoaqRxyzGEVrOqSfO5w5WIyQvQJkORCmF1J5bIubNl5uhQTFxvvOCvsKHKWw2RdZ9uzzWeg1zXkEFiuoPcEOOyFAS0L; pageview_counter.srs=12; s_nr30=1706264510690-Repeat; s_sq=%5B%5BB%5D%5D; _ga_3J0XCBB972=GS1.1.1706264507.35.1.1706264510.0.0.0; _ga=GA1.3.555592575.1703419592; nol_fpid=wagitpyybdlmdxdosnsfslyt8ayzm1703419591|1703419591881|1706264511099|1706264511259; reaidtok=eyJ1aWQiOiI0MDI4N2YwYTY5MDg0OWU3MDE2OTE5NmU0YzEzMGY5YiIsImVtYWlsVmVyaWZpZWQiOnRydWUsImV4cGlyeU1pbGxzIjoxNzA2MjY1NDEzMTg4fQ==.tAoEVeLZxYDvHcKGV/sdl1/Ont6nwC1RA8l4gK8UfT9ThO4E4dFTNYB6N/BWlR2/; reastok=NDAyODdmMGE2OTA4NDllNzAxNjkxOTZlNGMxMzBmOWI6MTcwNjI2NTQxMzE4ODp0WTJpcEFiOTRyaUpOMU5LYlJ2N1BhZGJZVGt6QUNxdDFiOEc3TDJ4cFZXNWVMZEJoT29TM0RtcUtZNXRSTUI4; reautok=eyJraWQiOiI1ODQzNzNlMy0xMjUxLTExZWEtYWQ3Yi00ZTAwYWMyYTA1MDUiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibGlkIjoiY2JmOTBhYmMtMjNmZi00ZjE1LTkxNDgtOWMzMDE1NDA0M2M5IiwiaXNzIjoiaHR0cHM6XC9cL3d3dy5yZWFsZXN0YXRlLmNvbS5hdSIsIm1mYV9lbmFibGVkIjpmYWxzZSwiZXhwIjoxNzA2MjY1NDEzLCJpYXQiOjE3MDYyNjQ1MTMsImVtYWlsIjoicmFraS5jaG93bHVyQGdtYWlsLmNvbSIsImp0aSI6ImI2K25acmlISHB2WHdUcGFnbnVqSkNtNEJPMD0iLCJjaWQiOiI0MDI4N2YwYTY5MDg0OWU3MDE2OTE5NmU0YzEzMGY5YiJ9.wRRm0Y6i3KbMrVI6aXy16JsHeMCafHW3tKWEOsiTqb81DoRQKxxDtIt2M_P13hXpfYGjtgHEJs-OdSm94FeuXeYudkycEsLcA4Smb8fb41CdoRWUg_wTRiDMTpYe13un-0VMJV51uRwXGKb99FXH0JQBTN_e0pt49n8Iz6tyQdjoVOWSUA9Yh_tCfJq7tjqCM_cxK5FY8wsgHl0HhfX-uDHAsjU4NpurHsDyTyJSL4zdgmcrJ3Le1AgvR4OeIfl7BUv_Yxt2Q3p4w0GYq9SDsrEI4vM7cqTTUYbINeEt2zKgL2bIIN1Y38dTQmw_ivDz4e6SZiO8gRPxjbosKZVrsQ; reauinf=eyJtbGlkIjoicmEqKipyQGdtKioqLmNvbSIsImdlaWQiOiI4ZDcyN2E3OTE2YmEyNzU5ODRjNGY5YmU1NzQwMWQ5MDFiYmRjYTg5NjJjZDkxYjIwOTM2YTU4ZWU1YmFhYzI2IiwiY2lkIjoiNDAyODdmMGE2OTA4NDllNzAxNjkxOTZlNGMxMzBmOWIiLCJsaWQiOiJjYmY5MGFiYy0yM2ZmLTRmMTUtOTE0OC05YzMwMTU0MDQzYzkiLCJpc05ld1VzZXIiOmZhbHNlLCJleHBpcnlNaWxsaXMiOjE3Mzc4MDA1MTMxOTJ9; utag_main=v_id018c9bb83a74000d8838174cbf2d0506f001e06700bd0$_sn35$_se6$_ss0$_st1706266315310$vapi_domainrealestate.com.au$dc_visit33$ses_id1706264506213%3Bexp-session$_pn2%3Bexp-session$_prevpagerea%3Abuy%3Asearch%20result%20-%20list%3Bexp-1706268115313$dc_event3%3Bexp-session$dc_regionap-southeast-2%3Bexp-session$ttd_uuide2db2851-d294-47bf-bc14-08c79383b16b%3Bexp-session$adform_uid7672441694095711386%3Bexp-session; _sp_id.2fe7=a60f7758-a9bf-4d4b-bb02-5173fae7a592.1703419592.33.1706264515.1706154111.3f742f14-0406-4857-acdb-7484e1ebbd13; ab.storage.sessionId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%2255cf31d8-8212-726c-b72e-60c1c83645fa%22%2C%22e%22%3A1706266315327%2C%22c%22%3A1706264507036%2C%22l%22%3A1706264515327%7D",
  "Referer": "https//www.realestate.com.au/buy/list-1?activeSort=list-date",
  "Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "\"Windows\"",
  "Sec-Fetch-Dest": "document",
  "Sec-Fetch-Mode": "navigate",
  "Sec-Fetch-Site": "same-origin",
  "Sec-Fetch-User": "?1",
  "Upgrade-Insecure-Requests": "1",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
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