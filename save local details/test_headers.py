# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 03:25:13 2024

@author: Rakesh
"""

import requests

headers = {
     'Accept'              : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
     'Accept-Encoding'     :  'gzip, deflate, br',
     'Accept-Language'     : 'en-US,en;q=0.9',
     'Cache-Control'       :  'max-age=0',
     'Cookie'             : 'mid=2328080861352116551; reauid=374ddc179d9b30005a83a465b1010000d4b61000; split_audience=d; VT_LANG=language%3Den-US; s_ecid=MCMID%7C29458859232723271432541469721906480428; _fbp=fb.2.1705280347010.1963140142; _gcl_au=1.1.2121029749.1705280347; topid=REAUID:374DDC179D9B30005A83A465B1010000D4B61000; _gid=GA1.3.1236649124.1706070556; External=%2FTRIPLELIFT%3D3517964327327929042453%2F_EXP%3D1736817621%2F_exp%3D1737610544; _sp_ses.2fe7=*; ab.storage.deviceId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%2294b62965-d023-e5cd-3afc-cefca8ec3a84%22%2C%22c%22%3A1705281367060%2C%22l%22%3A1706110642436%7D; ab.storage.userId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%22cbf90abc-23ff-4f15-9148-9c30154043c9%22%2C%22c%22%3A1705281367057%2C%22l%22%3A1706110642436%7D; Country=AU; fullstory_audience_split=A; AMCVS_341225BE55BBF7E17F000101%40AdobeOrg=1; AMCV_341225BE55BBF7E17F000101%40AdobeOrg=-330454231%7CMCIDTS%7C19747%7CMCMID%7C29458859232723271432541469721906480428%7CMCAAMLH-1706716932%7C8%7CMCAAMB-1706716932%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1706119332s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.1.2; s_cc=true; DM_SitId1464=1; DM_SitId1464SecId12707=1; pageview_counter.srs=1; s_nr30=1706112137155-Repeat; s_sq=%5B%5BB%5D%5D; _ga=GA1.1.1500484308.1705280348; nol_fpid=6uwqifudjkwtgsg9hvqsdeeelsxfn1705280347|1705280347070|1706112137459|1706112137469; DM_SitId1464SecId12708=1; reaidtok=eyJ1aWQiOiI0MDI4N2YwYTY5MDg0OWU3MDE2OTE5NmU0YzEzMGY5YiIsImVtYWlsVmVyaWZpZWQiOnRydWUsImV4cGlyeU1pbGxzIjoxNzA2MTUyNjM4NDAxfQ==.o4351uBWpNUyf51gXV8mzVsHJCG06+rx2xQrDfPKMTE7X4Cu894Zw+oQYYddPD4F; reastok=NDAyODdmMGE2OTA4NDllNzAxNjkxOTZlNGMxMzBmOWI6MTcwNjE1MjYzODQwMTppODFpN3ZkdkRhMjBXbWk0YWZFR21kcG1HVzhmd21CMWFDWFVTWHVGZmdhenVzK2FJbHo3amovMDV5UFRlODE2; reautok=eyJraWQiOiI1ODQzNzNlMy0xMjUxLTExZWEtYWQ3Yi00ZTAwYWMyYTA1MDUiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwibGlkIjoiY2JmOTBhYmMtMjNmZi00ZjE1LTkxNDgtOWMzMDE1NDA0M2M5IiwiaXNzIjoiaHR0cHM6XC9cL3d3dy5yZWFsZXN0YXRlLmNvbS5hdSIsIm1mYV9lbmFibGVkIjpmYWxzZSwiZXhwIjoxNzA2MTUyNjM4LCJpYXQiOjE3MDYxNTE3MzgsImVtYWlsIjoicmFraS5jaG93bHVyQGdtYWlsLmNvbSIsImp0aSI6ImZCcGJBSnFGSVR1NTBZbUE1RFRVYjc5a1dkTT0iLCJjaWQiOiI0MDI4N2YwYTY5MDg0OWU3MDE2OTE5NmU0YzEzMGY5YiJ9.wtPNAu6cZ1quWTTAFrZTbxvcd18jVX5vBvW0jTFk8AWHlJ_1mYHxVgm2uFm7Gs-lz0Dpn8ypG8RIDXZCkc1tC4KHdknpp3EOu_jDZU9enfnktNSbdZPBxS7Y6b0QP_l1GHe6OhTTxOx9_DLmdvjKIB6SyOFLJ-sP-OIQVw-tKcf-2j5lI0TZPG_wj1ZwLq5R6OTgBxd4fdIqDz-D3iuK-IuElq9Fod8hCmQJ8FpNFFCMpLylhpBje7SyhvEBW43nU6FCMKZBH9uBKnKfPJzQWpmG7szYXXMSmN_hyvb6yn9kl1P9fE3xM1di_XshSAXyKcijE70kjawaYFd5acxxAg; reauinf=eyJtbGlkIjoicmEqKipyQGdtKioqLmNvbSIsImdlaWQiOiI4ZDcyN2E3OTE2YmEyNzU5ODRjNGY5YmU1NzQwMWQ5MDFiYmRjYTg5NjJjZDkxYjIwOTM2YTU4ZWU1YmFhYzI2IiwiY2lkIjoiNDAyODdmMGE2OTA4NDllNzAxNjkxOTZlNGMxMzBmOWIiLCJsaWQiOiJjYmY5MGFiYy0yM2ZmLTRmMTUtOTE0OC05YzMwMTU0MDQzYzkiLCJpc05ld1VzZXIiOmZhbHNlLCJleHBpcnlNaWxsaXMiOjE3Mzc2ODc3Mzg0MDZ9; KP_UIDz-ssn=01ftb9NjtqlkKcZsMThVfs7bJ0ykG1bn3sJ6kULMykVQNYKgkHNEbyOVJub9HQMgmDmFuTIEFSEDC8ZDRMHH29ZxeBwFxq5pXRUKmM2uk0tbBKN5Qk8PiwEtRMq6eqKNy1QSByZ6yDh8OGpb80ugHpcryi5eRybnzXUx4mA2HifGzg8w4xMveNf3WmFEn; KP_UIDz=01ftb9NjtqlkKcZsMThVfs7bJ0ykG1bn3sJ6kULMykVQNYKgkHNEbyOVJub9HQMgmDmFuTIEFSEDC8ZDRMHH29ZxeBwFxq5pXRUKmM2uk0tbBKN5Qk8PiwEtRMq6eqKNy1QSByZ6yDh8OGpb80ugHpcryi5eRybnzXUx4mA2HifGzg8w4xMveNf3WmFEn; QSI_HistorySession=https%3A%2F%2Fwww.realestate.com.au%2F~1706112132993%7Chttps%3A%2F%2Fwww.realestate.com.au%2Fbuy%2Flist-1%3FactiveSort%3Dlist-date~1706112147729; utag_main=v_id:018d0aa119a30007cfad5dfa1c430506f001e06700fb8$_sn:6$_se:12$_ss:0$_st:1706113952750$vapi_domain:realestate.com.au$dc_visit:6$_prevpage:rea%3Abuy%3Asearch%20result%20-%20list%3Bexp-1706115752754$ses_id:1706110642365%3Bexp-session$_pn:4%3Bexp-session$dc_event:5%3Bexp-session$ttd_uuid:2fee35be-8ea5-4699-9905-0a2f00530f1e%3Bexp-session$dc_region:ap-southeast-2%3Bexp-session$adform_uid:2839544144651002793%3Bexp-session; _sp_id.2fe7=3692a20e-ae12-4386-9a91-90e4337088c2.1705280347.6.1706112153.1706108527.76297c62-19fd-4b43-9f35-60adf4e6f0e9; ab.storage.sessionId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%22bfacb934-304e-2fd7-ec49-b6c7dec8ea05%22%2C%22e%22%3A1706113952777%2C%22c%22%3A1706110642435%2C%22l%22%3A1706112152777%7D; _ga_F962Q8PWJ0=GS1.1.1706110621.5.1.1706112228.0.0.0; _ga_3J0XCBB972=GS1.1.1706110621.6.1.1706112228.0.0.0',
     'Referer'             :'https://www.realestate.com.au/',
     'Sec-Ch-Ua'           :'"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
     'Sec-Ch-Ua-Mobile'    :'?0',
     'Sec-Ch-Ua-Platform'  :' "Windows"',
     'Sec-Fetch-Dest'      :'document',
     'Sec-Fetch-Mode'      :'navigate',
     'Sec-Fetch-Site'      :'same-origin',
     'Sec-Fetch-User'      :'?1',
     'Upgrade-Insecure-Requests':'1',
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
     }
 
url = 'https://www.realestate.com.au/'
 
response = requests.get(url)