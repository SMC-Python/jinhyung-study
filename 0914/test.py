import requests

title = input('제목을 입력해라 하마새키 서현아 : ')
content = input('내용을 입력해라 잘생긴 정범아 : ')

response = requests.post(

    "https://controlc.com/index.php",

    params={
        'act': 'submit',
    },
    #post 신청하면 페이로드에 있는 form data
    data={
        "subdomain": '',
        "antispam": "1",
        "website": '',
        "branch": '6900e687',
        "paste_title": title,
        "input_text": content,
        "timestamp": '1503c4774cf81847fce13669ff49bc90',
        "paste_password": '',
        "code": '0',
    },
    #post 정상코드 200 뽑기 위해서 요청헤더가 원하는 방식으로 신청해주는 것.
    #Request Headers 요청헤더
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'referer': 'https://controlc.com/6900e687/new.php',
        'origin': 'https://controlc.com',
    }
)

with open( 'C:/Users/user/Desktop/0914/0914/test.html', 'w', encoding='utf-8' ) as f:
    f.write(response.text)


