# -*- coding: utf-8 -*-
from unittest import result
from flask import Flask, jsonify
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import os
import psycopg2
import announcement



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
    return 'hello world!!'

@app.route("/ann", methods = ['post'])
def announcement_input():
    response = {
        "version" : "2.0",
        "template": {
            "output" : [
                {
                    'simpleText':{
                        "test": '지역을 입력해주세요\n(예시: 평택시 -> 평택)'
                    }
                }
            ]
        }
    }
    
    return jsonify(response)



if __name__ == "__main__":
    #db_create()
    app.run(host='0.0.0.0', debug=True)