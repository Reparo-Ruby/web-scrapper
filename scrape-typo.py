import requests
from bs4 import BeautifulSoup

zara_bowls = "https://cottonon.com/ZA/typo/?lang=en_ZA&q=bowl"

bowls = requests.get(zara_bowls)
soup = BeautifulSoup(bowls.text, 'html.parser')
bowl_list = soup.find_all("div", {"class": "product-tile"})

bowls_on_sale = {}
for bowl in bowl_list:
    bowl_name = bowl.find("div", {"class":"product-name"}).text.replace('\n','')
    bowl_price = bowl.find("span", {"class":"product-sales-price"}).text.replace('\n','')
    bowls_on_sale[bowl_name] = bowl_price.replace(" ","")

print(bowls_on_sale)