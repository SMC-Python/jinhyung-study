from bs4 import BeautifulSoup

with open('./0915/test.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
url = soup.select_one('.input-copy > form > input')
print(url.attrs['value'])