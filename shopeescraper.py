import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
import pandas as pd
import numpy as np
from time import sleep
from random import randint
import time

##############################################################

driver = webdriver.Chrome()
siteurl = 'https://shopee.ph/'
driver.get(siteurl)
time.sleep(2)
# thai_button = driver.find_element('xpath', '//*[@id="modal"]/div[1]/div[1]/div/div[3]/div[1]/button')
# thai_button.click()
# time.sleep(3)
close_button = driver.execute_script('return document.querySelector("shopee-banner-popup-stateful").shadowRoot.querySelector("div.shopee-popup__close-btn")')
close_button.click()
time.sleep(1)
search = driver.find_element('xpath', '//*[@id="main"]/div/header/div[2]/div/div[1]/div[1]/div/form/input')
search.send_keys('ck perfume')
search.send_keys(Keys.ENTER)
time.sleep(60)

all_product_list = []
all_price_list = []
all_sales_list = []
all_links_list = []

#retrive all information in 1 page aka range(1)
for i in range(1):
    driver.execute_script("document.body.style.zoom='10%'")
    time.sleep(2)
    data = driver.page_source
    soup = bs4.BeautifulSoup(data, features="html.parser")
    products = soup.find_all('div', {'class': 'shopee-search-item-result__item'})
    for element in products:
        all_product = element.find_all('div', {'class':'ie3A+n bM+7UW Cve6sh'})
        if len(all_product) > 0:
            all_product_list.append(all_product[0].text)
        all_price = element.find_all('div', {'class': 'vioxXd rVLWG6'})
        if len(all_price) > 0:
            all_price_list.append(all_price[0].text)
        all_sales = element.find_all('div', {'class': 'ZnrnMl'})
        if len(all_sales) > 0:
            all_sales_list.append(all_sales[0].text)
        all_links = element.find_all('a', {'data-sqe': 'link'})
        if len(all_links) > 0:
            all_links_list.append(siteurl + all_links[0]['href'])
    driver.execute_script("document.body.style.zoom='100%'")
    time.sleep(3)
    next_button = driver.find_element('xpath', '//*[@id="main"]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/button[2]')
    next_button.click()

# list of dictionaries (aka json)
productlistings = []

if len(all_product_list) == len(all_price_list) == len(all_sales_list) == len(all_links_list):
    print(f"{len(all_product_list)} listings available.")
    
    #iterate over all products then merge their own details into a list of dictionaries
    for i in range(len(all_product_list)):
        productlistings.append({"product": all_product_list[i], \
            "price": all_price_list[i], \
            "sales": all_sales_list[i], \
            "links": all_links_list[i], \
            })
    
    with open('productlistings.json', 'w' , encoding="utf-8") as f:
        print(json.dumps(productlistings), file=f)



first_reviews = []
all_reviews = [] #JSON

driver = webdriver.Chrome()

for link in all_links_list:
    driver.get(link)
    time.sleep(2)
    data = driver.page_source
    soup = bs4.BeautifulSoup(data, features="html.parser")
    # find product ratings section
    comments = soup.find_all('div', {'class':'shopee-product-comment-list'})
    time.sleep(3)
    for element in comments:
        reviews = element.find_all('div', {'class':'Rk6V+3'})
        if len(reviews) > 0:
            first_reviews.append(reviews[0])

            # harvest textcontent per reviewer
            text_review = ""
            for content in reviews:
                text_review += content.text
            print("TEXTS: " + text_review + "\n")

        else: first_reviews.append('None')
        print("NEXT REVIEWER!!!")
    

with open('first_reviews.txt', 'w' , encoding="utf-8") as f:
    print(first_reviews, file=f)