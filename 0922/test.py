import requests
from bs4 import BeautifulSoup

title = input("제목을 입력하세요: ")
content = input("내용을 입력하세요: ")

response = requests.post(
    "https://controlc.com/index.php",
    params={
        'act': 'submit'
    },
    data={
        "subdomain": '',
        "antispam": "1",
        "website": '',
        "branch": '6900e687',
        "paste_title": title,
        "input_text": content,
        "timestamp": "1503c4774cf81847fce13669ff49bc90",
        "paste_password": '',
        "code": "0",
    } ,
    headers={
        "referer": "https://controlc.com/"
    }
)

soup = BeautifulSoup(response.text, 'html.parser')
url_element = soup.select_one('.input-copy input')
url = url_element.attrs['value']

response1 = requests.get(url)
soup1 = BeautifulSoup(response1.text, 'html.parser')
title_element = soup1.select_one('#pastecontainer > div > div:nth-child(2)')
title = title_element.get_text()

print('-- 미리보기 --')
print('생성된 제목은', title, '입니다')
print('생성된 URL은', url, '입니다')