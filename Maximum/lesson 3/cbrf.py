import requests
from bs4 import BeautifulSoup

#R01235

def get_course(course_id):
    return soup.find("Valute", ID=course_id).Value.text

response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
if response.status_code == 200:
    soup = BeautifulSoup(response.content, features="xml")
    