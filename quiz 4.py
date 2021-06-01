
import requests
import bs4
import csv
from time import sleep
from random import randint




file = open("random_stuff.csv", "w", encoding='UTF-8', newline="\n")
page = 1
file_obj = csv.writer(file)
file_obj.writerow(["Name","Price","Availability"])

while page < 6:
    url = f"https://nido.ge/samzareulos-teqnika/page-{page}"
    r = requests.get(url)
    content = r.text
    soup = bs4.BeautifulSoup(content,"html.parser")
    allitems = soup.find("div",{"class" :"ty-pagination-container cm-pagination-container","id":"pagination_contents"})
    stuff = allitems.find_all("div",{"class":"ty-column4"})

    for each in stuff:
        try:
            name = each.find("a", {"class": "product-title"})
            name1 = name.text
            price = each.find("span", {"class": "ty-price"})
            price1 = price.span.text
            availability = each.find("div", {"class": "ut2-gl__amount"})
            availability1 = availability.div.div.span.text.strip()
            file_obj.writerow([name1, price1, availability1])
        except: continue

    page+=1
    sleep(randint(15, 20))

