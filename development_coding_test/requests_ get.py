# requests 기본 내장모듈이 아니라 따로 개발자가 설치해주어야한다.

import requests

target = "http://google.com"
response = requests.get(url = target)
print(response.text)