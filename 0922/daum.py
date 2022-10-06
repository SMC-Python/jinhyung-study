import requests
from bs4 import BeautifulSoup

#https://auction.realestate.daum.net/iframe/v15/map_main.php?pcode=1100000000&lvm=4&level=10&lat=37.570997155319354&lng=127.01177247590469&result=99&yongdo=99&yongdo_detail=99&rvt=2
response = requests.post(
    'https://auction.realestate.daum.net/ajax/main_list.php',

    params={
        "addr1": "서울",
        'result': "99",
        'yongdo': '99',
        'yongdo_detail': '99',
        'sort': '04D',
    },
    data={
        'total': '1293',
        'block': '1',
        'start': '',
        'next': '',
        'addr1': '서울',
        'addr2': '',
        'addr3': '',
        'bubcd': '',
        'kye': '',
        'local_num': '',
        'var_period': '',
        'result': '99',
        'var_kind': '',
        'yuchalcnt': '',
        'gamprice': '',
        'lowprice': '',
        'bdarea': '',
        'daejiarea': '',
        'ipchaltype': '',
        'bdname': '',
        'special': '',
        'addshow': '',
        'sort': '04D',
        'subMenuIdx': '1',
    },
    headers={
        'Origin': 'https://auction.realestate.daum.net',
        'Referer': 'https://auction.realestate.daum.net/v15/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
)

# # encoding이 웹사이트에 있는 헤더중 content-type이 인코딩과 비슷한데 다음 부동산은 uft-8이 아닌 euc-kr로 되어있음
# with open( 'C:/Users/user/Desktop/0922/0922/test.html', 'w', encoding='euc-kr' ) as f:
#     f.write(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

list = soup.select('.row_order2')

for tr in list:
    print(tr.select_one('.checkbox_label').get_text())