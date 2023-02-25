import time
import bs4 #easier in extracting html elements
from selenium import webdriver #for dynamic pages and interactions like clicking and waiting
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

all_links_list = ["https://shopee.ph//CK-ETERNITY-EDT-100ML-i.250700043.19173102207?sp_atk=84080359-385e-43bf-9660-649247a92a6d&xptdk=84080359-385e-43bf-9660-649247a92a6d", "https://shopee.ph//AIKEDA-Scents-Long-lasting-inspired-perfume-Premium-Oil-Based-perfume-for-women-i.423471202.23919964850?sp_atk=ef85e17f-24a3-46b4-8bc1-079518e8d7ca&xptdk=ef85e17f-24a3-46b4-8bc1-079518e8d7ca", "https://shopee.ph//Authentic-CK-Eternity-for-Men-100ml-Scentro-Style-i.286768164.8273812079?sp_atk=f389407c-0079-4756-ae4d-c5bd7eb61fd7&xptdk=f389407c-0079-4756-ae4d-c5bd7eb61fd7", "https://shopee.ph//Like-CK-One-by-Calvin-Klein-You'll-love-our-U-YOU-Fragrance-Body-Spray-2.5oz-70.9g-i.92328166.13631362105?sp_atk=8786351e-8bb3-4f97-beeb-034f1526803b&xptdk=8786351e-8bb3-4f97-beeb-034f1526803b"]
# all_links_list = ["https://shopee.ph//AIKEDA-Scents-Long-lasting-inspired-perfume-Premium-Oil-Based-perfume-for-women-i.423471202.23919964850?sp_atk=ef85e17f-24a3-46b4-8bc1-079518e8d7ca&xptdk=ef85e17f-24a3-46b4-8bc1-079518e8d7ca"]

first_reviews = []
all_reviews = [] #JSON with structure [{producturl: "https://blabla", reviews: [{name: "as****ddd", stars: 5, date, comment}] }]

driver = webdriver.Chrome()

for link in all_links_list:
    driver.get(link)
    driver.execute_script("document.body.style.zoom='50%'")
    time.sleep(5)
    data = driver.page_source
    soup = bs4.BeautifulSoup(data, features="html.parser")

    product_url = driver.current_url
    
    print("SCRAPING " + driver.title)

    end_of_page = False
    while True:
        time.sleep(1)
        # Find product ratings section
        try:
            ratinglist2 = driver.find_element(By.CSS_SELECTOR, ".shopee-product-comment-list")
        except:
            break

        # Get the list of review cards
        comments2 = ratinglist2.find_elements(By.CSS_SELECTOR, ".shopee-product-rating")
        time.sleep(2)
        
        
        for element in comments2: 
            # Each element is a Review Card consisting of (reviewer pfp, reviewer censord name, stars, time/date and variation of product, optional comment, optional media)

            try: 
                review = element.find_element(By.CSS_SELECTOR, "div.Rk6V\+3")# extract optional comment (class Rk6V+3)  #convert to selenium
                if review:
                    first_reviews.append(review) #convert to selenium

                    # harvest textcontent per reviewer
                    text_review = ""
                    
                    text_review += review.text + "\t\n"

                    print("TEXTS: " + text_review)

                else: first_reviews.append('None') #convert to selenium
                print("------------------")

            except:
                break


        # Go next page if there is one
        nextbtn = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.shopee-page-controller.product-ratings__page-controller > button.shopee-icon-button.shopee-icon-button--right")))
        driver.execute_script("arguments[0].click();", nextbtn)

        finalbtn = driver.find_element(By.CSS_SELECTOR, 'div.shopee-page-controller.product-ratings__page-controller > button:nth-last-child(2)')

        if ("shopee-button-solid" in finalbtn.get_attribute("class") or (not nextbtn.is_displayed())):
            print("No more next pages")
            
            if end_of_page:
                break

            end_of_page = True

        print("\nClicked!->NEXT-PAGE>\n")

        time.sleep(2)

with open('first_reviews2.txt', 'w' , encoding="utf-8") as f:
    print(first_reviews, file=f)