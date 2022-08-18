# -*- coding: utf-8 -*-
from unittest import result
from flask import Flask, jsonify, request
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import psycopg2
import start


app = Flask(__name__)

@app.route("/")
def hello():
    return "Verson : 65"

# 사용자가 공고를 보기 원할 때 
@app.route("/api/anninputloc", methods=["post"])
def announcement_input():  
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])
    response = {
        "version" : "2.0",
        "template": {
            "outputs" : [
                {
                    'simpleText':{
                        "text": "지역을 입력해주세요\n(예시: 평택시 -> 평택)"
                    }
                }
            ]
        }
    }
    return jsonify(response)

@app.route('/api/sayHello', methods=['POST'])
def sayHello():
    body = request.get_json() # 사용자가 입력한 데이터
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "안녕 hello I'm Ryan"
                    }
                }
            ]
        }
    }

    return responseBody


# 지역입력 시 공고 출력
@app.route('/api/annout', methods=['POST'])
def location():
    
    body = request.get_json()
    print(body)
    # 카카오 챗봇에서 보낸 요청값을 body에 저장
    params_df=body['action']['params']
    print(params_df)
    # 카카오 챗봇에서 보낸 요청값 중 action -> params의 모든 정보 저장
    loc=params_df['loc']
    print(loc)
    # 사용자 발화값 중 입력값을 받기 위해 사용

    loc_li="'%" + loc + "%'"
    # loc list
    # sql 문법에 맞도록 형태 맞춰주기
    df1=start.db_select(loc_li)
    # db_select함수에 loc_li값 입력
    #print(df1)
    name=df1['name']
    print(name)
    print(type(name))
    # df1이라는 데이터프레임의 'name'컬럼값을 series형식으로 저장
    URL = df1['rink']
    # df1이라는 데이터프레임의 'rink'컬럼값을 series형식으로 저장
    if len(df1) > 0:
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "listCard": {
                            "header": {
                                "title": "공고 내역입니다."
                            },
                            "items": [
                                {
                                    "title": name[0],
                                    "imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                                    "link": {
                                        "web": URL[0]
                                    }
                                },
                                {
                                    "title": name[1],
                                    "imageUrl": "http://k.kakaocdn.net/dn/N4Epz/btqqHCfF5II/a3kMRckYml1NLPEo7nqTmK/1x1.jpg",
                                    "link": {
                                        "web": URL[1]
                                    }
                                },
                                {
                                    "title": name[2],
                                    "imageUrl": "http://k.kakaocdn.net/dn/bE8AKO/btqqFHI6vDQ/mWZGNbLIOlTv3oVF1gzXKK/1x1.jpg",
                                    "link": {
                                        "web": URL[2]
                                    }
                                }
                            ],
                            "buttons": [
                                {
                                    "label": "더보기",
                                    "action": "webLink",
                                    "webLinkUrl": "https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancListView.do#"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    else :
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "listCard": {
                            "header": {
                                "title": "공고 내역입니다."
                            },
                            "items": [
                                {
                                    "title": '현재 모집중인 공고가 없습니다.',
                                },
                            ],
                            "buttons": [
                                {
                                    "label": "다른공고더보기",
                                    "action": "webLink",
                                    "webLinkUrl": "https://www.applyhome.co.kr/ai/aia/selectAPTLttotPblancListView.do#"
                                }
                            ]
                        }
                    }
                ]
            }
        }


    
    return responseBody

