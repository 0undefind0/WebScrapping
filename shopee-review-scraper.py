import time
import bs4 #easier in extracting html elements
from selenium import webdriver #for dynamic pages and interactions like clicking and waiting
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# all_links_list = ["https://shopee.ph//CK-ETERNITY-EDT-100ML-i.250700043.19173102207?sp_atk=84080359-385e-43bf-9660-649247a92a6d&xptdk=84080359-385e-43bf-9660-649247a92a6d", "https://shopee.ph//AIKEDA-Scents-Long-lasting-inspired-perfume-Premium-Oil-Based-perfume-for-women-i.423471202.23919964850?sp_atk=ef85e17f-24a3-46b4-8bc1-079518e8d7ca&xptdk=ef85e17f-24a3-46b4-8bc1-079518e8d7ca"]
all_links_list = ["https://shopee.ph//AIKEDA-Scents-Long-lasting-inspired-perfume-Premium-Oil-Based-perfume-for-women-i.423471202.23919964850?sp_atk=ef85e17f-24a3-46b4-8bc1-079518e8d7ca&xptdk=ef85e17f-24a3-46b4-8bc1-079518e8d7ca"]

first_reviews = []
all_reviews = [] #JSON with structure [{producturl: "https://blabla", reviews: [{name: "as****ddd", stars: 5, date, comment}] }]

driver = webdriver.Chrome()

for link in all_links_list:
    driver.get(link)
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(7)
    data = driver.page_source
    soup = bs4.BeautifulSoup(data, features="html.parser")

    product_url = driver.current_url

    # find product ratings section
    ratinglist = soup.find_all('div', {'class':'product-ratings__list'})
    comments = ratinglist[0].find('div', {'class':'shopee-product-comment-list'})
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

    # Go next page if there is one
    nextbtn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.shopee-page-controller.product-ratings__page-controller > button.shopee-icon-button.shopee-icon-button--right")))
    driver.execute_script("arguments[0].click();", nextbtn)
    print("\n\n\nClicked!\n")

    time.sleep(2)

with open('first_reviews.txt', 'w' , encoding="utf-8") as f:
    print(first_reviews, file=f)