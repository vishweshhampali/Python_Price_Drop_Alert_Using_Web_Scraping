#https://towardsdatascience.com/web-scraping-with-beautiful-soup-a-use-case-fc1c60c8005d
#https://github.com/AlexTheAnalyst/PortfolioProjects/blob/main/Amazon%20Web%20Scraper%20Project.ipynb

#Importing libraries
"""
For these tasks, I chose to use the Requests: HTTP for Humans library.
GET request to the URL will send headers.
As we are using python 'User Agent' header will be something like 'python-requests/2.19.1'.
Basically this means someone is scraping the website using python.
As some websites block such requests we will define headers to behave as humanly as possible.
In order to look what headers are sent by browser please go to 'https://httpbin.org/get'.
From above mentioned URL copy "User-Agent" tag and substitute below. 
Read more about HTTP and Headers here 'https://www.seobility.net/en/wiki/HTTP_headers'.
Read more about requests library 'https://requests.readthedocs.io/en/latest/'.
"""
from bs4 import BeautifulSoup
import requests
#import time
#import datetime
#import smtlplib

#Connect to Website and pull in data

Flipkart_URL = 'https://www.flipkart.com/canon-eos-3000d-dslr-camera-1-body-18-55-mm-lens/p/itm6f665fea97bc2?pid=CAMF3DHJURPEMNRN&lid=LSTCAMF3DHJURPEMNRN5POEJU&marketplace=FLIPKART&q=canon+1200d+camera&store=jek%2Fp31%2Ftrv&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&fm=organic&iid=1c742629-dbc8-4eae-b0c9-623d0d7c1772.CAMF3DHJURPEMNRN.SEARCH&ppt=hp&ppn=homepage&ssid=3c3nanvia80000001676980351095&qH=44ee4b2066a82a77'
#Flipkart_URL = 'https://www.flipkart.com/google-pixel-4a-just-black-128-gb/p/itm023b9677aa45d?pid=MOBFUSBNAZGY7HQU&lid=LSTMOBFUSBNAZGY7HQUWHTF0C&marketplace=FLIPKART&q=pixel+4a&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=f4333c2a-bd28-4d14-a425-9031014ff94d.MOBFUSBNAZGY7HQU.SEARCH&ppt=sp&ppn=sp&ssid=qqnkai0qkw0000001677064038113&qH=614b192c242ae032'
#Amazon_URL = 'https://www.amazon.in/Canon-EOS-3000D-Digital-18-55mm/dp/B07BRWY6XV/ref=sr_1_1?crid=264F3DGHOZHZP&keywords=canon+EOS+3000d+DSLR&qid=1676980439&sprefix=canon+eos+3000d+dslr%2Caps%2C321&sr=8-1'
Amazon_URL = 'https://www.amazon.in/Canon-1500D-Digital-Camera-S18-55/dp/B07BS4TJ43/ref=dp_prsubs_1?pd_rd_w=7vYvR&content-id=amzn1.sym.37b67494-dbbc-4d44-83e6-6de40b4b120d&pf_rd_p=37b67494-dbbc-4d44-83e6-6de40b4b120d&pf_rd_r=GRZWNFVB2X2ARKP3A8VT&pd_rd_wg=P9FXv&pd_rd_r=42b28adc-fec5-407b-bb22-fc9c169ddacc&pd_rd_i=B07BS4TJ43&psc=1'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

"""
Using get method from requests library we will s store the URL response.
"""

Flipkart_page = requests.get(Flipkart_URL, headers = headers)
Amazon_page = requests.get(Amazon_URL, headers = headers)

#print(Flipkart_page.content)
#print(Amazon_page.content)

"""
Everything contained in that webpage is now in the page object.
In order to parse this (HTML)pages we will use Beautiful Soup (BS4) library. 
BS4 is a Python library for parsing HTML and XML documents. 
It provides simple methods to navigate, search, and modify parse trees. 
"""

Flipkart_soup = BeautifulSoup(Flipkart_page.content, "html.parser")
Amazon_soup = BeautifulSoup(Amazon_page.content, "html.parser")

"""
BS4 has some very useful functions which make traversing through tags very easy.
You can through them here :
In our case we will use find() and get_text() to get data.
"""
#print(Flipkart_soup)
#print(Amazon_soup)

#Flipkart_soup = Flipkart_soup.prettify()
#Amazon_soup =  Amazon_soup.prettify()

#print(Flipkart_soup)
#print(Amazon_soup)

"""
With Inspect Element tool in browser you can look for HTML tags under which data is present.
Copy id of the tag to navigate.
Use Screenshots.
"""
Flipkart_Title = Flipkart_soup.find_all('span',attrs={"class":"B_NuCI"})[0].get_text()
Flipkart_Title = Flipkart_Title.strip()

Amazon_Title = Amazon_soup.find(id='productTitle').get_text()
Amazon_Title = Amazon_Title.strip()

Flipkart_Availability = Flipkart_soup.find_all('div',attrs={"class":"_16FRp0"})
if (len(Flipkart_Availability)==0):
    Flipkart_Availability = 'In stock'
else:
    Flipkart_Availability = Flipkart_Availability[0].get_text()
Flipkart_Availability = Flipkart_Availability.strip()

Amazon_Availability = Amazon_soup.find(id='availability').get_text()
Amazon_Availability = Amazon_Availability.strip()
#print(Amazon_Availability.strip())

if (Flipkart_Availability == 'In stock'):
    Flipkart_Price = Flipkart_soup.find_all('div',attrs={"class":"_30jeq3 _16Jk6d"})[0].get_text()
    Flipkart_Price = Flipkart_Price.strip()
    Flipkart_Price = Flipkart_Price[1:]
else:
    Flipkart_Price = 0


if (Amazon_Availability == 'In stock'):
    Amazon_Price = Amazon_soup.find(id='corePriceDisplay_desktop_feature_div').get_text()
    Amazon_Price = Amazon_Price.strip()
    Amazon_Price = Amazon_Price.split('₹')[1]
else :
    Amazon_Price = 0

#Amazon_Price = Amazon_soup.find(id='corePriceDisplay_desktop_feature_div').get_text()
#print(Amazon_soup.find(id='outOfStock').get_text())
#print(Amazon_Price)
print(Amazon_Title)
print(Amazon_Availability)
print(Amazon_Price)

print(Flipkart_Title)
print(Flipkart_Availability)
print(Flipkart_Price)