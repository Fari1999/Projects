#vorher pip install requests Beautifulsoup
import requests
from bs4 import BeautifulSoup

URL = "https://sonnenaufgang.online/sun/velbert"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser") #ist html
sunrise_data = soup.find("li",{"data-name": "sunrise"}) 
sunrise_data = sunrise_data.text #Gibt nur den Text aus
print(sunrise_data)
