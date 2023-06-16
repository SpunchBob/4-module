import requests
from bs4 import BeautifulSoup

#R01235

def get_course():
    return soup.find("Valute", ID="R01235").Value.text

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
if response.status_code == 200:
    soup = BeautifulSoup(response.content, features="xml")
    