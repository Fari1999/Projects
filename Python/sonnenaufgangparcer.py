#vorher pip install requests Beautifulsoup
import requests
from bs4 import BeautifulSoup

URL = "https://sonnenaufgang.online/sun/velbert"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser") #ist html
sunrise_data = soup.find("li",{"data-name": "sunrise"}) #findet man in entwickler tools der website ob li o. span, data-name, sunrise
sunset_data = soup.find("li",{"data-name":"sunset"})
riseangle_data = soup.find("li",{"data-name":"riseangle"})

sunrise_data = sunrise_data.text #Gibt nur den Text aus
sunset_data = sunset_data.text
riseangle_data = riseangle_data.text

print(sunrise_data, sunset_data, riseangle_data)
