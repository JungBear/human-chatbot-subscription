# -*- coding: utf-8 -*-
from unittest import result
from flask import Flask, jsonify, request
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import psycopg2
import database

app = Flask(__name__)

@app.route("/")
def hello():
    database.db_create()
    return "Verson : 97"

@app.route("/api/hello")
def test():
    req = request.get_json()
    response = {
        "version" : "2.0",
        "template": {
            "outputs" : [
                {
                    'simpleText':{
                        "text": "안녕하세요"
                    }
                }
            ]
        }
    }

# 사용자가 공고를 보기 원할 때 
@app.route("/api/anninputloc", methods=["post"])
def announcement_input():  
    req = request.get_json()
    print(req)
    print(req['userRequest']['utterance'])
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
    req = request.get_json() # 사용자가 입력한 데이터
    print(req)
    print(req['userRequest']['utterance'])

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
    
    req = request.get_json()
    print(req)
    # 카카오 챗봇에서 보낸 요청값을 body에 저장
    loc=req['action']['params']['loc']
    print(loc)
    # 사용자 발화값 중 입력값을 받기 위해 사용
    df1=database.area_db(loc)
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

@app.route('/api/score', methods=['POST'])
def score():
    try:
    # try-except는 예외처리문법
    #  - 코드를 실행하는 중에 발생한 에러를 처리할때 사용
    #  - 에러가 났을때 코드가 멈추지않고 계속 실행되게 사용
    #  - 프로그램이 멈추는 현상 방지
        req = request.get_json()
        print(req)
        # 카카오챗봇에서 요구받은값 출력
        # heroku logs를 터미널에 입력하면 값을 볼 수 있음
        sco1 = req['action']['detailParams']['sys_text1']["value"]
        #'action/detailParams/sys_text1/value'의 값이 첫번째 조건의 입력값이 된다
        sco2 = req['action']['detailParams']['sys_text2']["value"]
        # 두번째 조건의 입력값
        sco3 = req['action']['detailParams']['sys_text3']["value"]
        # 세번째 조건의 입력값
        print('sco1의 값입니다:',sco1)
        print('sco2의 값입니다:',sco2)
        print('sco3의 값입니다:',sco3)
        print(type(sco1))
        score1 = int(sco1)
        score2 = int(sco2)  
        score3 = int(sco3)
        print(type(score1))
        # 형변환 str -> int

        score_list1 = database.score_db1(sco1)
        # 리스트의 형태로 입력받는다
        score_end1 = score_list1[0][0]
        print(score_end1)
        # 조건1의 결괏값
        # 리스트의 형태 중 내가 원하는 인덱스값 불러오기
        score_list2 = database.score_db1(sco2)
        score_end2 = score_list2[1][0]
        # 조건2의 결괏값
        score_list3 = database.score_db1(sco3)
        print(score_list3)
        # 조건3의 값이 조건2의값보다 크다
        # 조건3의 값이 조건2의 값보다 크면 리스트에 값이 입력이 안된다
        if len(score_list3) == 2:
            # 조건3의 값 > 조건2의 값
            # 조건2의 값이 입력이안되어서 원래의 리스트의 갯수가 3개가 되어야하는데 2개가된다
            # 그래서 리스트 갯수 = 2일 때로 지정
            score_end3 = score_list3[1][0]
            
        else:
            score_end3 = score_list3[2][0]
            # 조건3 <= 조건2일때
            # 원래대로 리스트의 갯수가 3개가 된다
        print(score_end3)
        result = score_end1 + score_end2 + score_end3
        print(result)
        # 우리가 필요한 값은 조건1, 2, 3의 총 합이므로 변수를 하나 설정해 준다
        # result = int
    except:
    # 에러가 났을 경우 실행
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": '잘못입력하셨습니다'
                        }
                    }
                ]
            }
        }
    else:
    # 에러가 나지 않았을 경우 실행
        responseBody = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": '조건1의 점수는 : {0} \n조건2의 점수는 : {1}\n조건3의 점수는 : {2}\n총합은 : {3}점 입니다.'.format(score_end1, score_end2, score_end3, result)
                            # format매서드를 써서 변수값을 입력 가능하게 해준다.
                            # {0}=score_end1, {1}=score_end2, {2}=score_end3, {3}=result
                        }
                    }
                ]
            }
        }
    return responseBody
