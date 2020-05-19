import requests
from bs4 import BeautifulSoup
import time
import pandas


time.sleep(1)
main_page = requests.get("https://www.nike.com/w/mens-shoes-nik1zy7ok")
time.sleep(1)
print(main_page)

soup = BeautifulSoup(main_page.content, "html.parser")



product_name = []
product_name_div = soup.find_all('div', class_ = "product-card__title")
for items in product_name_div:
    product_name.append(items.text)

    

type_list = []
type_div = soup.find_all('div', class_ = "product-card__subtitle")
for items in type_div:
    type_list.append(items.text)

    
price_list = []

price_div = soup.find_all('div', class_ = "css-b9fpep")
for items in price_div:
    price_list.append(items.text)



shoe_list = {"shoe_name": [], "shoe_type": [], "shoe_price": []}

for i in product_name:
    shoe_list["shoe_name"].append(i)


for i in type_list:
    shoe_list["shoe_type"].append(i)
    
for i in price_list:
    shoe_list["shoe_price"].append(i)
    
    
    
print(shoe_list)

df = pandas.DataFrame(shoe_list)
df.to_csv('shoe_list_exported.csv', index = False )
    

