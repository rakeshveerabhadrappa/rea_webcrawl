# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 22:11:25 2024

@author: Rakesh
"""
import json
import os

text = """Accept:
text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding:
gzip, deflate, br
Accept-Language:
en-AU,en-GB;q=0.9,en-US;q=0.8,en;q=0.7
Cache-Control:
max-age=0
Cookie:
_scid=1398931f-c59a-4705-bdcf-40546bdd7c28; _cs_c=1; __pdst=3d7b8c045b46455a9d874d52ddbf8c71; _fbp=fb.1.1706778936665.622772877; locale=vic; AAMC_tatts_0=REGION%7C8; device-id=2cb2beff-2a95-421d-97d1-b88dc6d87d99; AMCV_2C03C2D754DCC8640A4C98C6%40AdobeOrg=MCMID%7C04953959590107545591152921504606846975; s_ecid=MCMID%7C04953959590107545591152921504606846975; nllastdelid=b605506; aam_uuid=04920409394861281691149566485082220585; at_check=true; AMCVS_2C03C2D754DCC8640A4C98C6%40AdobeOrg=1; TLC768=!OUQD+HGu37C19pBUOQBJpzJFg9Nl7u6H7fG7LQ9vA3RA7TiX1ehyB+w5YZSaxFTWLqfc2N+WO8w0Q1uNmreG8bQBTwoJGmdKEE7jvGhE; _cs_mk_aa=0.8245325568042894_1707557197224; s_vnum=1738314937559%26vn%3D3; s_invisit=true; s_cp_persist=L_NTL_THELOTT_NA_SEARCH_AO_SEM; s_lv_s=More%20than%207%20days; s_cm=undefinedwww.google.comOther%20Natural%20Referrersundefined; s_kw=%5B%5B%27n%2Fa%27%2C%271707557197226%27%5D%5D; s_cc=true; s_cvp=%5B%5B%27EDM%257CtattsDM212104%27%2C%271706779250073%27%5D%2C%5B%27L_NTL_THELOTT_NA_SEARCH_AO_SEM%27%2C%271707557197229%27%5D%5D; s_cpm=%5B%5B%27Unknown%2520Paid%2520Channel%27%2C%271706779244843%27%5D%2C%5B%27Other%2520Natural%2520Referrers%27%2C%271707557197232%27%5D%5D; _sctr=1%7C1707483600000; adcloud={%22_les_lsc%22:%221707557196323%2Cthelott.com%2C1715423196%22%2C%22_les_v%22:%22y%2Cthelott.com%2C1707559014%22}; mbox=PC#966cd00d268d4090986deff1ac61914f.36_0#1770802015|session#50845b2535344538b70814c269ac0665#1707559075; AMCV_2C03C2D754DCC8640A4C98C6%40AdobeOrg=-432600572%7CMCMID%7C04953959590107545591152921504606846975%7CMCIDTS%7C19764%7CMCAID%7CNONE%7CMCOPTOUT-1707564414s%7CNONE%7CMCAAMLH-1708162014%7C8%7CMCAAMB-1708162014%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CvVersion%7C4.5.2; _scid_r=1398931f-c59a-4705-bdcf-40546bdd7c28; _cs_id=9b945d2a-fa67-af34-a3f0-39b50f8b53ac.1706778936.4.1707557214.1707557196.1.1740942936304.1; _cs_s=3.0.0.1707559014655; _uetsid=7d2ea230c7f611eeadc36bbd7cc0ebdf; _uetvid=75de04b0c0e211eeb021f786a4435da0; s_sq=%5B%5BB%5D%5D; s_nr=1707557559627-Repeat; s_lv=1707557559627; RT="z=1&dm=www.thelott.com&si=ca33dbb1-f75a-4a62-a94c-97ca69330be6&ss=lsfvgrmm&sl=3&tt=3un&bcn=%2F%2F684d0d4a.akstat.io%2F&ul=g556"
Referer:
https://www.thelott.com/mon-wed-gold-lotto/results
Sec-Ch-Ua:
"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"
Sec-Ch-Ua-Mobile:
?1
Sec-Ch-Ua-Platform:
"Android"
Sec-Fetch-Dest:
document
Sec-Fetch-Mode:
navigate
Sec-Fetch-Site:
same-origin
Sec-Fetch-User:
?1
Upgrade-Insecure-Requests:
1
User-Agent:
Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36"""


text = text.replace(':','')
lines = text.split('\n')
data_dict = {}
for key, value in zip(lines[0::2], lines[1::2]):
    # Remove leading and trailing whitespaces from key and value
    key = key.strip()
    value = value.strip()

    # Add the key-value pair to the dictionary
    data_dict[key] = value

json_string = json.dumps(data_dict, indent=2)  # indent parameter for pretty formatting

folder_path = "../net_info"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
file_path = folder_path+"/response_header.json"

# Dump the dictionary to a JSON file
with open(file_path, 'w') as json_file:
    json.dump(json_string, json_file, indent=2)  # indent parameter for pretty formatting (optional)

print(f"header has been dumped to {file_path}")
 
#%%


