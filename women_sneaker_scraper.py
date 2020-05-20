# This script is a web scapper using a combination of BeautifulSoup and Selenium to parse and retrieve data from the Nike Website

import requests
from bs4 import BeautifulSoup
import time
import pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

# This funtion was slighlty modified for out purposes and was originaly taken from https://dev.to/hellomrspaceman/python-selenium-infinite-scrolling-3o12

def scroll(driver, timeout):
    """
        Used to scroll through the entirety of Nike's Men's sneakers collection. 
        
        Args:
            driver : web automation framework that allows us to scroll indefinelty.
            timeout (int): time in between scrolls.  
    """
    
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

product_links = []
# Here we are using soup object to find all the links to Women's shoe on the Nike website
# We are storing these links for later use
for a in soup.find_all('a', class_ = "product-card__link-overlay", href=True):
    product_links.append(a['href'])
print(product_links)
holder = []
shoe_d ={"shoe_name": "", "shoe_type": "", "shoe_color": "", "shoe_price": "", "shoe_size": "", "shoe_link": ""}      

# This for loop essentially parses through every link we collected from the products and are "clicked" in order to access the data on every shoe
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
    
    # Finding name, type, and price of shoe. In a try/except because we do not want incomplete data in the dictionaries we will be creating
    try:
        
        title_div = soup.find('h1', class_=["headline-2", "css-33lwh4"])
        item_name = title_div.text
        
        type_div = soup.find('h2', class_ = ["headline-5-small", "pb1-sm", "d-sm-ib", "css-6yhqc5"])
        item_type = type_div.text
        
        price_div = soup.find("div", {"data-test":"product-price-reduced"})
        
        if price_div == None:
            price_div = soup.find("div", {"data-test":"product-price"}) # discount price
            item_price = price_div.text
            
        else:
            item_price = price_div.text
         
    except:
        print("did not work continue 1")
        continue
    
# Gathering sizes and colors of shoes    
    try:
           
        shoe_size_label = soup.find_all("label", class_= "css-xf3ahq")
        for size in shoe_size_label:
            item_size = size.text
            
            shoe_color_li = soup.find_all('li', class_ = "description-preview__color-description ncss-li")
            for color in shoe_color_li:
                item_color = color.text
        
                # Creating dictionaries which will be populated with shoe data   
                shoe_d ={"shoe_name": item_name, "shoe_type": item_type, "shoe_color": item_color, "shoe_price": item_price, "shoe_size": item_size, "shoe_link": item_link}     
                
                print(shoe_d)
                holder.append(shoe_d)
    except:
        
        print("did not work continue 2")
        continue
    
# Using pandas to create a dataframe that will contain instance of Women'a sneakers from Nike        
df = pandas.DataFrame(holder)

# Exported to a csv for later use
df.to_csv('women_shoe_dict_exported.csv', index = False )
