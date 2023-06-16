import requests
from bs4 import BeautifulSoup

response = requests.get("https://2ch.hk/b/arch/2017-09-10/res/160781668.html")
soup = BeautifulSoup(response.text, "html.parser")

first_past = soup.find("blockquote", {"id": "m160782000"})
first = first_past.text.strip()


second_past = soup.find("blockquote", {"id": "m160781807"})
second = second_past.text.strip()


third_past = soup.find("blockquote", {"id": "m160782406"})
third = third_past.text.strip()


fourth_past = soup.find("blockquote", {"id": "m160784090"})
fourth = fourth_past.text.strip()


fiveth_past = soup.find("blockquote", {"id": "m160784509"})
fiveth = fiveth_past.text.strip()

pastas = [first, third, fourth, fiveth]
