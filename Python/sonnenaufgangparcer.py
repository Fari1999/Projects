import requests
from bs4 import BeautifulSoup

URL = "https://sonnenaufgang.online/sun/velbert"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
sunrise_data = soup.find("li",{"data-name": "sunrise"})
sunrise_data = sunrise_data.text
print(sunrise_data)
