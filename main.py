import requests 
 
url = 'https://shopee.ph/CK-BE-200ml-AUTHENTIC-PERFUME-for-men-from-US-PERFFUME-LONG-LASTING-i.684490038.20636154466?sp_atk=8ed03602-b314-4fae-b254-c624a2568602&xptdk=8ed03602-b314-4fae-b254-c624a2568602' 
 
response = requests.get(url) 
 
html = response.text 
 
# print(html)

with open('scraped.html', 'w') as f:
    print(html, file=f)