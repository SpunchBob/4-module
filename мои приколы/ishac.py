import requests
from bs4 import BeautifulSoup

import xml

def items():
    names_items = soup.find("div", {"class": "items-container rebirth"})
    print(names_items.text)

response = requests.get("https://isaac-items.ru/")
soup = BeautifulSoup(response.text, "html.parser" )

items()

