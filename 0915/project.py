from urllib import response
import requests
from bs4 import BeautifulSoup

response = requests.get(
    'https://controlc.com/0f22a531',

)

soup = BeautifulSoup(response.text, 'html.parser')
header = soup.select_one('#pastecontainer > div > div:nth-child(2)')

print(header.get_text())