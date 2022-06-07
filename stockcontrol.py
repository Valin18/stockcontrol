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




url = 'https://www.amazon.com/Cooler-Backpack-Insulated-Waterproof-Beach/dp/B08V3YJQ15/ref=sr_1_5?keywords=Everlasting+Comfort+Insulated+Cooler+Backpack&qid=1654626604&sr=8-5'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.70'}

page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
span = soup.find(id='availability')








clear()
print(span)
