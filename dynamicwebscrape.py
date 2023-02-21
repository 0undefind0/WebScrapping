from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
import time



#[0221/165126.029:INFO:CONSOLE(1)] "A preload for 'https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg//assets/ProductDetailsPage.954d5bb98220d4f7.js' is found, but is not used because the request credentials mode does not match. Consider taking a look at crossorigin attribute.", source: https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg//assets/webpack-runtime.a610edf0173c55b0.js (1)
# var cors = require('cors');    
# app.use(cors({credentials: true, origin: 'http://localhost:5000'}))


# instantiate options 
options = webdriver.ChromeOptions() 
 
# run browser in headless mode 
# options.headless = True #this si deprecated
options.add_argument('--headless')
 
# instantiate driver 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 
 
# load website 
url = 'https://shopee.ph/CK-BE-200ml-AUTHENTIC-PERFUME-for-men-from-US-PERFFUME-LONG-LASTING-i.684490038.20636154466?sp_atk=8ed03602-b314-4fae-b254-c624a2568602&xptdk=8ed03602-b314-4fae-b254-c624a2568602'
 
# get the entire website content 
driver.get(url) 

time.sleep(3)

# select elements by class name 
# elements = driver.find_elements(By.CLASS_NAME, 'shopee-product-rating') 
elements = driver.find_elements(By.CSS_SELECTOR, '#main > div > div:nth-child(3) > div.Sxova7 > div > div.page-product > div.container > div.UwHWuz > div.page-product__content > div.page-product__content--left > div:nth-child(2) > div > div > div.product-ratings__list > div.shopee-product-comment-list')

for review in elements: 
 print("found one")
	# select H2s, within element, by tag name 
 texts = review.find_element(By.TAG_NAME, 'div').text
	# print H2s 
 print(review)




# with open('selenium_scraped.html', 'w', encoding="utf-8") as f:
#     print(driver.page_source, file=f)