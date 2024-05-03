# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 23:33:38 2024

@author: Backpack1
"""

from bs4 import BeautifulSoup
import requests

headers ={
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "en-US,en;q=0.9",
  "Cache-Control": "max-age=0",
  "Cookie": "mid=2328080861352116551; reauid=374ddc179d9b30005a83a465b1010000d4b61000; split_audience=d; VT_LANG=language%3Den-US; s_ecid=MCMID%7C29458859232723271432541469721906480428; _fbp=fb.2.1705280347010.1963140142; _gcl_au=1.1.2121029749.1705280347; topid=REAUID374DDC179D9B30005A83A465B1010000D4B61000; _gid=GA1.3.1236649124.1706070556; External=%2FTRIPLELIFT%3D3517964327327929042453%2F_EXP%3D1736817621%2F_exp%3D1737610544; KP_UIDz-ssn=01kAfRZns6eHl0c1xWOYdeJ6mwFREqMEjbVwrfNHCfKSgZBNbjbMLE0yu4RjZzzj7HPKsdKSv9y3y4fnbuSXHW3iiCOGvabJuTsVGhmeDSTg3Prmi2FuzmE3VVgk8UirYFeD56O9dtFW8cddqdBoS476jxhmxvnDBTaMwWL50bPKJugpXDKVOelPVdVlb; KP_UIDz=01kAfRZns6eHl0c1xWOYdeJ6mwFREqMEjbVwrfNHCfKSgZBNbjbMLE0yu4RjZzzj7HPKsdKSv9y3y4fnbuSXHW3iiCOGvabJuTsVGhmeDSTg3Prmi2FuzmE3VVgk8UirYFeD56O9dtFW8cddqdBoS476jxhmxvnDBTaMwWL50bPKJugpXDKVOelPVdVlb; tracking_acknowledged=true; Country=AU; fullstory_audience_split=B; s_nr30=1706181153269-Repeat; _sp_ses.2fe7=*; reaidtok=eyJ1aWQiOiI0MDI4N2YwYTY5MDg0OWU3MDE2OTE5NmU0YzEzMGY5YiIsImVtYWlsVmVyaWZpZWQiOnRydWUsImV4cGlyeU1pbGxzIjoxNzA2MTgyMDUzNTQxfQ==.yKOBltntUtZUHPbaqnau1bX2TSWnSTHsAKLw0NX+jS8A+eP1Cwun9PanEEZazuv3; reastok=NDAyODdmMGE2OTA4NDllNzAxNjkxOTZlNGMxMzBmOWI6MTcwNjE4MjA1MzU0MTpzRjRaNWw5NTltQm1hSTdmeERBMW00VHkva1BBZjFuWkZrcDRkbm44U20xL2VYbXVlTEVZTXQ5eFFWdE92Y0ZH; reautok=eyJraWQiOiI1ODQzNzNlMy0xMjUxLTExZWEtYWQ3Yi00ZTAwYWMyYTA1MDUiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibGlkIjoiY2JmOTBhYmMtMjNmZi00ZjE1LTkxNDgtOWMzMDE1NDA0M2M5IiwiaXNzIjoiaHR0cHM6XC9cL3d3dy5yZWFsZXN0YXRlLmNvbS5hdSIsIm1mYV9lbmFibGVkIjpmYWxzZSwiZXhwIjoxNzA2MTgyMDUzLCJpYXQiOjE3MDYxODExNTMsImVtYWlsIjoicmFraS5jaG93bHVyQGdtYWlsLmNvbSIsImp0aSI6ImNRSDVBY2x5UUJBemhRSmRsOE1aQU1Vd2F2TT0iLCJjaWQiOiI0MDI4N2YwYTY5MDg0OWU3MDE2OTE5NmU0YzEzMGY5YiJ9.TFlfcp0zFQvsVgAOM-PSEyE1O-TMjCeynvECBnM2iYh4ayMENu_VdD3PvB4SO73SI0s5icUAJmEvtaPuchHty7EgDfHMJ8JEltBrBO1vev0mnymAi82b3qqiMvwoiIVzKxlHGGbuYK0Gd26wz3Z3nD3jJ7Pev0S5S6PC4NsRXkXUMeeEjjcah38OmC2JVSfukKn4Jn5JemH5JyLjPX04xt6praePE-1HD-cIxrOWQiSUTtUcUC5H0Z6qWW5mV7EpdL__O-Oj4-idoMVA0PQOfkKzf8GvEo82WxBqwiyfLk6K7n77GVPZYdTfFJGJP9PICcxM92TIc9lwCLeRcQ2LuQ; reauinf=eyJtbGlkIjoicmEqKipyQGdtKioqLmNvbSIsImdlaWQiOiI4ZDcyN2E3OTE2YmEyNzU5ODRjNGY5YmU1NzQwMWQ5MDFiYmRjYTg5NjJjZDkxYjIwOTM2YTU4ZWU1YmFhYzI2IiwiY2lkIjoiNDAyODdmMGE2OTA4NDllNzAxNjkxOTZlNGMxMzBmOWIiLCJsaWQiOiJjYmY5MGFiYy0yM2ZmLTRmMTUtOTE0OC05YzMwMTU0MDQzYzkiLCJpc05ld1VzZXIiOmZhbHNlLCJleHBpcnlNaWxsaXMiOjE3Mzc3MTcxNTM1NDZ9; _sp_id.2fe7=3692a20e-ae12-4386-9a91-90e4337088c2.1705280347.9.1706181154.1706174118.cc8c7056-1a62-4aa0-8ba1-3a8d45503132; AMCVS_341225BE55BBF7E17F000101%40AdobeOrg=1; AMCV_341225BE55BBF7E17F000101%40AdobeOrg=-330454231%7CMCIDTS%7C19747%7CMCMID%7C29458859232723271432541469721906480428%7CMCAAMLH-1706785953%7C8%7CMCAAMB-1706785953%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1706188353s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; s_cc=true; utag_main=v_id018d0aa119a30007cfad5dfa1c430506f001e06700fb8$_sn9$_se2$_ss0$_st1706182953624$vapi_domainrealestate.com.au$dc_visit7$ses_id1706181153173%3Bexp-session$_pn1%3Bexp-session$_prevpagerea%3Ahomepage%3Bexp-1706184753628$dc_event2%3Bexp-session$dc_regionap-southeast-2%3Bexp-session; ab.storage.deviceId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%2294b62965-d023-e5cd-3afc-cefca8ec3a84%22%2C%22c%22%3A1705281367060%2C%22l%22%3A1706181153703%7D; ab.storage.userId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%22cbf90abc-23ff-4f15-9148-9c30154043c9%22%2C%22c%22%3A1705281367057%2C%22l%22%3A1706181153703%7D; ab.storage.sessionId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%22311ad5e6-8400-c069-4f4a-0ff4b0c536f7%22%2C%22e%22%3A1706182953713%2C%22c%22%3A1706181153702%2C%22l%22%3A1706181153713%7D; DM_SitId1464=1; DM_SitId1464SecId12707=1; _gat_gtag_UA_143679184_2=1; _ga_F962Q8PWJ0=GS1.1.1706181155.7.0.1706181155.0.0.0; _ga=GA1.1.1500484308.1705280348; _ga_3J0XCBB972=GS1.1.1706181155.8.0.1706181155.0.0.0; nol_fpid=6uwqifudjkwtgsg9hvqsdeeelsxfn1705280347|1705280347070|1706181155265|1706181155566; QSI_HistorySession=https%3A%2F%2Fwww.realestate.com.au%2F~1706181158130",
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
        file.write(response.body.decode('utf-8', 'ignore'))
    soup = BeautifulSoup(response.text, 'html.parser')
    property_price = soup.select_one('span.property-price').get_text(strip=True)
    print(property_price)
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")