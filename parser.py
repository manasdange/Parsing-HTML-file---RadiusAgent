#This file was created for RadiusAgent online assignment
#Author: Manas Dange
#Date: 30/07/2020

#Importing libraries
from bs4 import BeautifulSoup
import json

#Function defined to extract text from bs4 objects
def get_text(obj):
    if not len(obj)==0:
        return obj[0].text.strip()

#Loading and parsing the HTML File
html = open('New Lead  (3).html', 'r').read()
soup = BeautifulSoup(html, features="html.parser")

#Extracting objects
name = email = phone = address = ""

name_obj = soup.select('body > table > tr:nth-child(3) > td > table > tr:nth-child(1) > td.block > table > tr:nth-child(8) > td.aligncenter > font > strong')
name = get_text(name_obj)
    

email_obj = soup.select('body > table > tr:nth-child(3) > td > table > tr.block > td.width280 > table > tr:nth-child(4) > td > font > a')
email = get_text(email_obj)

phone_obj = soup.select('body > table > tr:nth-child(3) > td > table > tr.block > td.width280 > table > tr:nth-child(3) > td')
phone = get_text(phone_obj)

address_obj = soup.select('body > table > tr:nth-child(8) > td:nth-child(2) > table > tr > td > table > tr:nth-child(2) > td > font:nth-child(1) > strong > a')
address = get_text(address_obj)

#Dumping to JSON
data_dict = {"name": name, "email": email, "phone": phone, "address": address}

with open("output.json", "w") as f:
    json.dump(data_dict, f)