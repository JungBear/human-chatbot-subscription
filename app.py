# -*- coding: utf-8 -*-
from unittest import result
from flask import Flask, jsonify, request
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import psycopg2
from announcement import df, input_region, region



'''
## DB 연결 Local
def db_create():
    # 로컬
    engine = create_engine("postgresql://postgres:1234@localhost:5432/chatbot", echo = False)
		
		# Heroku
    engine = create_engine("postgresql://xnrniyjhurkuos:b0d752cc9e29106fb8c4b1f7cd39c985a5a23bb67a35d8c365a6175355e9bf13@ec2-50-19-255-190.compute-1.amazonaws.com:5432/dashvvhprslttt", echo = False)

    engine.connect()
    engine.execute("""
        CREATE TABLE IF NOT EXISTS announcement(
            주택명 TEXT,
            주택상세구분명 TEXT,
            공급위치 TEXT,
            모집공고일 TEXT,
            청약접수시작일 TEXT,
            청약접수종료일 TEXT,
            당첨자발표일 TEXT,
            홈페이지주소 TEXT
        );"""
    )
    data = pd.read_csv('data/area.csv')
    #print(data)
    data.to_sql(name='announcement', con=engine, schema = 'public', if_exists='replace', index=False)
'''

app = Flask(__name__)

@app.route("/")
def hello():
    return 'hello world!!!!!'

@app.route("/ann_input", methods = ["post"])
def announcement_input():
    request_data = json.loads()
    
    response = {
        "version" : "2.0",
        "template": {
            "output" : [
                {
                    'simpleText':{
                        "test": "지역을 입력해주세요\n(예시: 평택시 -> 평택)"
                    }
                }
            ]
        }
    }
    return jsonify(response)

@app.route('/ann_output', methods=["post"])
def announcement_output():
    # 카카오톡 서버에서 스킬이 보내는 요청의 데이터
    request_data = json.loads(request.get_data(), encoding = 'utf-8')
    print(request_data)
    # 파라미터에서 지역파라미터의 값 가져오기(문자열로 되어있어 별도로 json으로 변환)
    params = request_data['action']['params']
    param_loc = json.loads(params['loc'])
    
    print(param_loc) 
    loc_input = input_region(param_loc)

    print(input_region)
    response = {
        "version": "2.0",
        "template": {
           "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": "공고 입니다."
                        },
                        "items": [
                            {
                                "title": df[['Name']],
                                "description": "새로운 AI의 내일과 일상의 변화",
                                "imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                                "link": {
                                    "web": df[['Rink']]
                                }
                            },
                            {
                                "title": "챗봇 관리자센터",
                                "description": "카카오톡 채널 챗봇 만들기",
                                "imageUrl": "http://k.kakaocdn.net/dn/N4Epz/btqqHCfF5II/a3kMRckYml1NLPEo7nqTmK/1x1.jpg",
                                "action": "block",
                                "blockId": "62654c249ac8ed78441532de",
                                "extra": {
                                    "key1": "value1",
                                    "key2": "value2"
                                }
                            },
                            {
                                "title": "Kakao i Voice Service",
                                "description": "보이스봇 / KVS 제휴 신청하기",
                                "imageUrl": "http://k.kakaocdn.net/dn/bE8AKO/btqqFHI6vDQ/mWZGNbLIOlTv3oVF1gzXKK/1x1.jpg",
                                "action": "message",
                                "messageText": "Kakao i Voice Service",
                                "extra": {
                                    "key1": "value1",
                                    "key2": "value2"
                                }
                            }
                        ],
                        "buttons": [
                            {
                                "label": "구경가기",
                                "action": "block",
                                "blockId": "62654c249ac8ed78441532de",
                                "extra": {
                                    "key1": "value1",
                                    "key2": "value2"
                                }
                            }
                        ]
                    }
                }
            ]
        }
    }
    return jsonify(response)




if __name__ == "__main__":
    #db_create()
    app.run(port=5000,debug=True)