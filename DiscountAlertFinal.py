#https://towardsdatascience.com/web-scraping-with-beautiful-soup-a-use-case-fc1c60c8005d
#https://github.com/AlexTheAnalyst/PortfolioProjects/blob/main/Amazon%20Web%20Scraper%20Project.ipynb
#https://medium.com/@modularcoder/writing-a-coding-tutorial-article-on-medium-the-technical-parts-34ea1e5fcd61
"""
Importing libraries
"""

from bs4 import BeautifulSoup
import requests
import smtplib
import csv 
import datetime
import os.path
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()

sender = "vaidya.kare@gmail.com"
recipients = ["vishweshhampali@gmail.com"]
password = "yfvjflmehenezdyl"



"""
Connect to Website and pull in data
"""
x = 'https://www.flipkart.com/logitech-gamepad-f310/p/itmdyfyfrzch29cf?pid=ACCDYFXZ6QEUZEFZ&lid=LSTACCDYFXZ6QEUZEFZIISO8W&marketplace=FLIPKART&q=controller&store=4rr%2Fkm5%2Fr39%2Fa7g%2Fy7a&spotlightTagId=TrendingId_4rr%2Fkm5%2Fr39%2Fa7g%2Fy7a&srno=s_1_5&otracker=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_9_na_na_na&fm=search-autosuggest&iid=01b3d6f3-06c0-449b-a2af-9d3fd8e91cbb.ACCDYFXZ6QEUZEFZ.SEARCH&ppt=sp&ppn=sp&ssid=mjbnhasl2o0000001678195519116&qH=594c103f2c6e04c3'
y = 'https://www.amazon.in/Logitech-G-940-000112-F310-Gamepad/dp/B0757QFBRL/ref=sr_1_4?crid=YSVEB0DD6CAB&keywords=logitech+controller+for+pc&qid=1678195661&s=computers&sprefix=logitech+controller+for+pc%2Ccomputers%2C182&sr=1-4'
#Flipkart_URL = 'https://www.flipkart.com/canon-eos-3000d-dslr-camera-1-body-18-55-mm-lens/p/itm6f665fea97bc2?pid=CAMF3DHJURPEMNRN&lid=LSTCAMF3DHJURPEMNRN5POEJU&marketplace=FLIPKART&q=canon+1200d+camera&store=jek%2Fp31%2Ftrv&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&fm=organic&iid=1c742629-dbc8-4eae-b0c9-623d0d7c1772.CAMF3DHJURPEMNRN.SEARCH&ppt=hp&ppn=homepage&ssid=3c3nanvia80000001676980351095&qH=44ee4b2066a82a77'
#Amazon_URL = 'https://www.amazon.in/Canon-1500D-Digital-Camera-S18-55/dp/B07BS4TJ43/ref=dp_prsubs_1?pd_rd_w=7vYvR&content-id=amzn1.sym.37b67494-dbbc-4d44-83e6-6de40b4b120d&pf_rd_p=37b67494-dbbc-4d44-83e6-6de40b4b120d&pf_rd_r=GRZWNFVB2X2ARKP3A8VT&pd_rd_wg=P9FXv&pd_rd_r=42b28adc-fec5-407b-bb22-fc9c169ddacc&pd_rd_i=B07BS4TJ43&psc=1'

Flipkart_URL = x
Amazon_URL = y

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}


"""
For these tasks, I chose to use the 'Requests: HTTP for Humans' library.
GET request to the URL will send headers.
As we are using python 'User Agent' header will be something like 'python-requests/2.19.1'.
Basically this means someone is scraping the website using python.
As some websites block such requests we will define headers to behave as humanly as possible.
In order to look what headers are sent by browser please go to 'https://httpbin.org/get'.
From above mentioned URL copy "User-Agent" tag and substitute below. 
Read more about HTTP and Headers here 'https://www.seobility.net/en/wiki/HTTP_headers'.
Read more about requests library 'https://requests.readthedocs.io/en/latest/'.
"""



"""
Using get method from requests library we will s store the URL response.
"""

Flipkart_page = requests.get(Flipkart_URL, headers = headers)
Amazon_page = requests.get(Amazon_URL, headers = headers)

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

"""
With Inspect Element tool in browser you can look for HTML tags and their Id or classes under which data is present.
Copy id or class of the tag to navigate.
Use Screenshots.
"""

"""
Using find_all and get_text method from BS4 for fetching Flipkart title.
"""

Flipkart_Title = Flipkart_soup.find_all('span',attrs={"class":"B_NuCI"})[0].get_text()
Flipkart_Title = Flipkart_Title.strip()

"""
Using find_all and get_text method from BS4 for fetching Flipkart title.
"""

Amazon_Title = Amazon_soup.find(id='productTitle').get_text()
Amazon_Title = Amazon_Title.strip()


"""
Similarly using above mentioned functions fetching availability and depending on that fetching product prices.
And if product is unavailable setting product price to 0.
"""

Flipkart_Availability = Flipkart_soup.find_all('div',attrs={"class":"_16FRp0"})
if (len(Flipkart_Availability)==0):
    Flipkart_Availability = 'In stock'
else:
    Flipkart_Availability = Flipkart_Availability[0].get_text()
Flipkart_Availability = Flipkart_Availability.strip()

Amazon_Availability = Amazon_soup.find(id='availability').get_text()
Amazon_Availability = Amazon_Availability.strip()
Amazon_Availability_Split = Amazon_Availability.lower().split()


if (Flipkart_Availability == 'In stock'):
    Flipkart_Price = Flipkart_soup.find_all('div',attrs={"class":"_30jeq3 _16Jk6d"})[0].get_text()
    Flipkart_Price = Flipkart_Price.strip()
    Flipkart_Price = Flipkart_Price[1:]
    Flipkart_Price = int(Flipkart_Price.replace(',',''))
else:
    Flipkart_Price = 0


if ('out' not in Amazon_Availability_Split):
    Amazon_Price = Amazon_soup.find(id='corePriceDisplay_desktop_feature_div').get_text()
    Amazon_Price = Amazon_Price.strip()
    Amazon_Price = Amazon_Price.split('₹')[1]
    Amazon_Price = int(Amazon_Price.replace(',',''))
else :
    Amazon_Price = 0

"""
Using Python's os.path library which has some useful functions for pathnames to check if file is already created or not.
Using Python's datetime library to get timestamp at which program was run. This timestamo will be added in CSV file generated
to store product prices over the period.
"""
file_path = r'D:/ProjectWebScraper/DiscountAlert.csv'

flag = os.path.isfile(file_path)

filename = "DiscountAlert.csv"
current_datetime = datetime.datetime.now()

Amazon_price_list = []
Flipkart_price_list = []

"""
If CSV file already exists then data from file is fetched to find minimum price of the product over the period and if product price scraped now
is equal or less than that minimum price then and email alert is sent to the user.
"""




if flag:
    with open(filename, 'r') as csvfile:

        csvreader =  csv.reader(csvfile)
        header = next(csvreader)

        for row in csvreader:
            #print(row[-1])
            Flipkart_price_list.append(int(row[-1].replace(',','')))
            
            #print(row[-2])
            Amazon_price_list.append(int(row[-2].replace(',','')))
    if '0' in Flipkart_price_list:         
        Flipkart_price_list.remove('0')
    if '0' in Amazon_price_list:
        Amazon_price_list.remove('0')

    if ((Amazon_Price <= min(Amazon_price_list)) and (Amazon_Price != 0)) or ((Flipkart_Price <= min(Flipkart_price_list)) and (Flipkart_Price != 0)):

        if Amazon_Price < Flipkart_Price:
            subject = "Alert!! Maybe you can buy these products now."
            body = str(Amazon_Title) + " is " + str(Amazon_Availability).lower() + " now " + "and at a minimum price of " + str(Amazon_Price) + "."
            body = body + "\n" + str(Amazon_URL)
            send_email(subject, body, sender, recipients, password)
        else:
            subject = "Alert!! Maybe you can buy these products now."
            body = str(Flipkart_Title) + " is " + str(Flipkart_Availability).lower() + " now " + "and at a minimum price of " + str(Flipkart_Price) + "."
            body = body + "\n" + str(Flipkart_URL)
            send_email(subject, body, sender, recipients, password)

else:

    print("No data")


"""
If CSV is not present i.e there is no prior data or program is being run first time then the file will be created and data will 
be appended to the file.
Else data will be directly appended to the CSV file.
"""



fields = ['Date_Time','Amazon_Product','Flipkart_Product','Amazon_Price','Flipkart_Price']

row = [str(current_datetime),Amazon_Title,Flipkart_Title,Amazon_Price,Flipkart_Price]




if flag:
    with open(filename, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(row)

    
else:

    with open(filename, 'w', newline='') as csvfile:
    
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(fields)


        csvwriter.writerow(row)

    




print("End")