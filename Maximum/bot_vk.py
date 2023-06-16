import requests
from bs4 import BeautifulSoup

import vk_api
import random

response = requests.get("https://swapi.dev/api/planets/")
soup = BeautifulSoup(response.content, "html.parser")

print(soup)