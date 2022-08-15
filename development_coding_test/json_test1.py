import json

# 사전 자료형(dict) 데이터 선언
user = {
    "id" : "gildong",
    "password": "1!2@3#4$",
    "age": 30,
    "hobby" : ["football", "programming"]
}

# 파이썬 변수를 JSON 객체로 변환
# indent는 들여쓰기에서 공백 몇번 사용할지
json_data = json.dumps(user, indent = 4)
print(json_data)