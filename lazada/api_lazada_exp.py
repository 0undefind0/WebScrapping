import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('lazada/lazadaAPI.env')
load_dotenv(dotenv_path=dotenv_path)

import requests

url = "https://lazada-datahub.p.rapidapi.com/item_search"

querystring = {"q":"laptop stand","region":"PH","page":"1"}

headers = {
	"X-RapidAPI-Key": os.getenv('X-RapidAPI-Key'),
	"X-RapidAPI-Host": "lazada-datahub.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

with open('lazada/result.json', 'w', encoding='utf-8') as f:
    f.write(response.text)
    if len(response.text) > 0: print("Success")