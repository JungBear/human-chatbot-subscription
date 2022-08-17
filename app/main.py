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
    return "43"

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
    params_df=body['action']['params']
    print(params_df)
   
    loc=params_df['loc']
    print(loc)
    print(type(loc))

    loc_li="'%" + loc + "%'"
    df1=start.db_select(loc_li)
    print(df1)
    name=df1['Name']
    print(name)
    print(type(name))
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
                                "title": '123',
                                "description": "새로운 AI의 내일과 일상의 변화",
                                "imageUrl": "http://k.kakaocdn.net/dn/APR96/btqqH7zLanY/kD5mIPX7TdD2NAxgP29cC0/1x1.jpg",
                                "link": {
                                    "web": "https://namu.wiki/w/%EB%9D%BC%EC%9D%B4%EC%96%B8(%EC%B9%B4%EC%B9%B4%EC%98%A4%ED%94%84%EB%A0%8C%EC%A6%88)"
                                }
                            },
                            {
                                "title": '123',
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
                                "title": '123',
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
                                "label": "더보기",
                                "action": "block",
                                "link": "https://www.naver.com/",
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

    return responseBody
