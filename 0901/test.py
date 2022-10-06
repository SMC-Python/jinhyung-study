#pip install requests
import requests

# 기본 사이트 url, code 등 보려면 개발자모드 f12 누르고 network -> Headers

# protocol - domain - path - parameters
# http,https -- ~~.com -- / ~ ? -- key=value & key=value ~~

# ex) https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=가나다 
# ex) https://dict.naver.com/search.dict?dicQuery=test&query=test&target=dic&ie=utf8&query_utf=&isOnlyViewEE=

#requests 값을 되돌려줌 -> response
response = requests.get(

    #protocol
    "https://dict.naver.com/search.dict",

    #parameters
    params={
        # key : value
        'dicQuery' : 'test',
        'target' : 'dic',
        'query_utf' : '',
        'ie' : 'utf8',
        'query' : 'test',
        'isOnlyViewEE' : '',
    }
)

# C 바탕화면에 있는 0901 파일 안에 temp.html를 오픈하고 작성한다는 의미
with open('C:/Users/user/Desktop/0901/temp.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

#response 명령어 중 status_code = 200을 돌려줌
#response 명령어 중 text = html 코드를 돌려줌
