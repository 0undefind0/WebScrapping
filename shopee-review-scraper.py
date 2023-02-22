import time
import bs4
from selenium import webdriver

all_links_list = ["https://shopee.ph//CK-ETERNITY-EDT-100ML-i.250700043.19173102207?sp_atk=84080359-385e-43bf-9660-649247a92a6d&xptdk=84080359-385e-43bf-9660-649247a92a6d", "https://shopee.ph//P125-each-minimum-of-10pcs-85ml-RMG-Perfume-(free-hi-quality-multi-purpose-pouch-every-10pcs-85ml)-i.295927972.3846392077?sp_atk=ac3d6302-1d3a-4346-a93c-329a00fb64b2&xptdk=ac3d6302-1d3a-4346-a93c-329a00fb64b2"]

first_reviews = []
all_reviews = [] #JSON with structure [{producturl: "https://blabla", reviews: [{name: "as****ddd", stars: 5, date, comment}] }]

driver = webdriver.Chrome()

for link in all_links_list:
    driver.get(link)
    time.sleep(4)
    data = driver.page_source
    soup = bs4.BeautifulSoup(data, features="html.parser")

    product_url = driver.current_url

    # find product ratings section
    comments = soup.find_all('div', {'class':'shopee-product-comment-list'})
    time.sleep(3)
    for element in comments:
        # Each element is a Review Card consisting of (reviewer pfp, reviewer censord name, stars, time/date and variation of product, optional comment, optional media)

        reviews = element.find_all('div', {'class':'Rk6V+3'}) # extract optional comment (class Rk6V+3)
        if len(reviews) > 0:
            first_reviews.append(reviews[0])

            # harvest textcontent per reviewer
            text_review = ""
            for content in reviews:
                text_review += content.text + "\t\n"
            print("TEXTS: " + text_review)

        else: first_reviews.append('None')
        print("NEXT REVIEWER!!!")

    

with open('first_reviews.txt', 'w' , encoding="utf-8") as f:
    print(first_reviews, file=f)