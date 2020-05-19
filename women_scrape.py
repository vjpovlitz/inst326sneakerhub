import requests
from bs4 import BeautifulSoup
import time
import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
# from selenium.webdriver.firefox.options import Options

def scroll(driver, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height
 
# Setup the driver. This one uses firefox with some options and a path to the geckodriver
driver = webdriver.Safari()
# implicitly_wait tells the driver to wait before throwing an exception
driver.implicitly_wait(30)
# driver.get(url) opens the page
driver.get("https://www.nike.com/w/womens-shoes-5e1x6zy7ok")
# This starts the scrolling by passing the driver and a timeout
scroll(driver, 5)
# Once scroll returns bs4 parsers the page_source
soup = BeautifulSoup(driver.page_source, "html.parser")
# Them we close the driver as soup_a is storing the page source

# time.sleep(1)
# main_page = requests.get("https://www.nike.com/w/mens-shoes-nik1zy7ok")
# time.sleep(1)
# print(main_page)

# soup = BeautifulSoup(main_page.content, "html.parser")

product_links = [] 
for a in soup.find_all('a', class_ = "product-card__link-overlay", href=True):
    product_links.append(a['href'])
print(product_links)
    
    # if a == "https://www.nike.com/t/off-white™-waffle-racer-womens-shoe-cdQ473/CD8180-400":
    #     pass
    # if requests.get(a.status_code) == 200:
    #     product_links.append(a['href'])
    # else:   
    #     continue
# print(product_links)
    
# shoe_size = []
# shoe_color = []
holder = []
shoe_d ={"shoe_name": "", "shoe_type": "", "shoe_color": "", "shoe_price": "", "shoe_size": "", "shoe_link": ""}      


for every_link in product_links:
    item_link = every_link
    print(item_link)
    if every_link == "https://www.nike.com/t/off-white™-waffle-racer-womens-shoe-cdQ473/CD8180-001":
        pass
    elif every_link == "https://www.nike.com/t/off-white™-vapor-street-womens-shoe-KC6WqX/CD8178-001":
        pass
    elif every_link == "https://www.nike.com/t/off-white™-vapor-street-womens-shoe-KC6WqX/CD8178-700":
        pass
    else:
        time.sleep(2)
        driver.get(every_link)
        time.sleep(2)
    
    
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    
    #product_name_div = soup.find_all('div', class_ = "product-card__info")
    #for items in product_name_div:
    try:
        #title_div = soup.find('div', class_ = "product-card__title") 
        title_div = soup.find('h1', class_=["headline-2", "css-33lwh4"])
        item_name = title_div.text
        
        type_div = soup.find('h2', class_ = ["headline-5-small", "pb1-sm", "d-sm-ib", "css-6yhqc5"])
        item_type = type_div.text
        
        #price_div = soup.find('div', class_ = "css-b9fpep") # not on sale
        price_div = soup.find("div", {"data-test":"product-price-reduced"})
        if price_div == None:
            #price_div = soup.find('div', class_= "css-i260wg")
            price_div = soup.find("div", {"data-test":"product-price"}) # discount price
            item_price = price_div.text
        else:
            item_price = price_div.text
        print(item_name, item_type, item_price)    
    except:
        print("did not work continue 1")
        continue
    try:   
        shoe_size_label = soup.find_all("label", class_= "css-xf3ahq")
        for size in shoe_size_label:
            item_size = size.text
            
            shoe_color_li = soup.find_all('li', class_ = "description-preview__color-description ncss-li")
            for color in shoe_color_li:
                item_color = color.text
        
                print(item_color, item_size)    
                shoe_d ={"shoe_name": item_name, "shoe_type": item_type, "shoe_color": item_color, "shoe_price": item_price, "shoe_size": item_size, "shoe_link": item_link}     
                print(shoe_d)
                holder.append(shoe_d)
    except:
        print("did not work continue 2")
        continue
        
        












# for every_link in product_links:
#     time.sleep(.5)
#     driver.get(every_link)
#     time.sleep(.5)
#     soup3 = BeautifulSoup(driver.page_source, "lxml")
#     shoe_size_label = soup3.find_all("label", class_= "css-xf3ahq")
#     for items in shoe_size_label:
#         shoe_size.append(items.text)
        
#     shoe_color_li = soup3.find_all('li', class_ = "description-preview__color-description ncss-li")
    
#     for items in shoe_color_li:
#         shoe_color.append(items.text)
#         print(items.text)

    
# price_list = []
# product_name = []
# product_name_div = soup.find_all('div', class_ = "product-card__info")
# for items in product_name_div:
#     try:
#         title_div = items.find('div', class_ = "product-card__title") # not on sale
#         product_name.append(title_div.text)
#         price_div = items.find('div', class_ = "css-b9fpep") # not on sale
#         if price_div == None:
#             price_div = items.find('div', class_= "css-i260wg")
#         price_list.append(price_div.text)
#     except:
#         continue
        
        
    
# # product_name = []
# # product_name_div = soup.find_all('div', class_ = "product-card__title")
# # for items in product_name_div:
# #     product_name.append(items.text)
  

# type_list = []
# type_div = soup.find_all('div', class_ = "product-card__subtitle")
# for items in type_div:
#     type_list.append(items.text)
   

    
# # price_list = []

# # price_div = soup.find_all('div', class_ = "css-b9fpep") # not on sale
# # price_div2 = soup.find_all('div', class_= "css-i260wg") # on sale 
# # for items in price_div:
# #     price_list.append(items.text)
# #     print(items.text)
    
# # for ditems in price_div2:
# #     price_list.append(ditems.text)
# #     print(ditems.text)
# new_price_list = []
# for i in price_list:
#     new_price = str(i[1:])
#     new_price_list.append(new_price)

# new_shoe_color_list=[]   
# for i in shoe_color:
#     new_shoe_color = i[7:]
#     new_shoe_color_list.append(new_shoe_color)
    
    
    
    
# shoe_dict = { "shoe_name": product_name, "shoe_type": type_list, "shoe_color": new_shoe_color_list, "shoe_price": new_price_list, "shoe_size": shoe_size, "shoe_link": product_links}
# # shoe_dict = [{"shoe_name": []}, {"shoe_type": []}, {"shoe_price": []}, {"shoe_color": []}, {"shoe_link": []}]

# for i in product_name:
#     shoe_dict["shoe_name"].append(i)


# for i in type_list:
#     shoe_dict["shoe_type"].append(i)
    

    
    
# for i in product_links:
#     shoe_dict["shoe_link"].append(i)
    
df = pandas.DataFrame(holder)

df.to_csv('women_shoe_dict_exported.csv', index = False )
