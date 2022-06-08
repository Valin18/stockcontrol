import time
import smtplib
from traceback import print_exception
import requests
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
import os
from kutuphaneler import *


clear()

url1 = 'https://www.amazon.com/Cooler-Backpack-Insulated-Waterproof-Beach/dp/B08V3YJQ15/ref=sr_1_5?keywords=Everlasting+Comfort+Insulated+Cooler+Backpack&qid=1654626604&sr=8-5'
url2 = 'https://www.amazon.com/Disney-Lightyear-Interactive-Talking-Action/dp/B07PQFT83F/ref=sr_1_2?crid=133BRD8M2BMGB&keywords=Disney+Toy+Story+12"+Buzz+Lightyear&qid=1654709880&sprefix=disney+toy+story+12+buzz+lightyear%2Caps%2C429&sr=8-2'
url3 = 'https://www.amazon.com/Disney-Pixar-Talking-Action-Figure/dp/B08KXTWZH9/ref=sr_1_1_sspa?crid=FG296MIV64XQ&keywords=Disney+Pixar+Zurg+Talking+Action+Figure&qid=1654710171&sprefix=disney+pixar+zurg+talking+action+figure%2Caps%2C188&sr=8-1-spons&psc=1&smid=ARUHDLVVAHC1S&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMDUyQ0M3SDEwOVNBJmVuY3J5cHRlZElkPUEwNDg1NDcyMjQ5UVEzRTNVNkZaTSZlbmNyeXB0ZWRBZElkPUEwMTgxMDk2M0ZPQ1RLSFIwODRGRSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
url4 = 'https://www.amazon.com/TOURIT-Insulated-Backpack-Leakproof-Lightweight/dp/B07BVKY2F8/ref=sr_1_5'
url5 = 'https://www.amazon.com/TOURIT-Insulated-Backpack-Leakproof-Lightweight/dp/B07BVKY49D/ref=sr_1_5?crid=IS9B6WQ7IBU2&keywords=tourit%2Binsulated%2Bbackpack%2Bcooler%2B30%2Bcans%2Bleakproof&qid=1654712344&sprefix=tourit%2Binsulated%2Bbackpack%2Bcooler%2B28%2Bcans%2Bleakproof%2Caps%2C611&sr=8-5&th=1'
url6 = 'https://www.amazon.com/TOURIT-Insulated-Backpack-Leakproof-Lightweight/dp/B08BCJQJ46/ref=sr_1_5?crid=IS9B6WQ7IBU2&keywords=tourit%2Binsulated%2Bbackpack%2Bcooler%2B30%2Bcans%2Bleakproof&qid=1654712344&sprefix=tourit%2Binsulated%2Bbackpack%2Bcooler%2B28%2Bcans%2Bleakproof%2Caps%2C611&sr=8-5&th=1'
headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}



page1 = requests.get(url1,headers=headers)
soup1 = BeautifulSoup(page1.content, 'html.parser')
span1 = soup1.find('span', class_='a-size-medium a-color-success').get_text()
if span1 == "    In Stock.   ":
    print("Everlasting Comfort Insulated Cooler Backpack:%s ✔️\n" % soup1.find('span', class_='a-size-medium a-color-success').get_text())
    time.sleep(1)
else:
    print("Everlasting Comfort Insulated Cooler Backpack:%s ❌\n" % soup1.find('span', class_='a-size-medium a-color-success').get_text())
    time.sleep(1)





page2 = requests.get(url2,headers=headers)
soup2 = BeautifulSoup(page2.content, 'html.parser')
span2 = soup2.find('span', class_='a-size-medium a-color-success').get_text()
if span2 == "    In Stock.   ":
    print("Disney Toy Story 12 Buzz Lightyear:%s ✔️\n" % span2)
    time.sleep(1)
else:
    print("Disney Toy Story 12 Buzz Lightyear:%s ❌\n" % span2)
    time.sleep(1)






page3 = requests.get(url3,headers=headers)
soup3 = BeautifulSoup(page3.content, 'html.parser')
span3 = soup3.find('span', class_='a-size-medium a-color-success').get_text()
if span3 == "    In Stock.   ":
    print("Disney Pixar Zurg Talking Action Figure:%s ✔️\n" % span3)
    time.sleep(1)
else:
    print("Disney Pixar Zurg Talking Action Figure:%s ❌\n" % span3)
    time.sleep(1)




page4 = requests.get(url4,headers=headers)
soup4 = BeautifulSoup(page4.content, 'html.parser')
span4 = soup4.find('span', class_='a-size-medium a-color-success').get_text()
if span4 == "    In Stock.   ":
    print("TOURIT Cooler Backpack 30 Cans Lightweight |BLACK|:%s ✔️\n" % span4)
    time.sleep(1)
else:
    print("TOURIT Cooler Backpack 30 Cans Lightweight |BLACK|:%s ❌\n" % span4)
    time.sleep(1)





page5 = requests.get(url5,headers=headers)
soup5 = BeautifulSoup(page5.content, 'html.parser')
span5 = soup5.find('span', class_='a-size-medium a-color-success').get_text()
if span5 == "    In Stock.   ":
    print("TOURIT Cooler Backpack 30 Cans Lightweight |GRAY|:%s ✔️\n" % span5)
    time.sleep(1)
else:
    print("TOURIT Cooler Backpack 30 Cans Lightweight |GRAY|:%s ❌\n" % span5)
    time.sleep(1)




page6 = requests.get(url6,headers=headers)
soup6 = BeautifulSoup(page6.content, 'html.parser')
span6 = soup6.find('span', class_='a-size-medium a-color-success').get_text()
if span6 == "    In Stock.   ":
    print("TOURIT Cooler Backpack 30 Cans Lightweight |DARK GRAY|:%s ✔️\n" % span6)
    time.sleep(1)
else:
    print("TOURIT Cooler Backpack 30 Cans Lightweight |DARK GRAY|:%s ❌\n" % span6)
    time.sleep(1)




