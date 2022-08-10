# -*- coding: utf-8 -*-
from flask import Flask
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

## DB 연결 Local
def db_create():
    # 로컬
    engine = create_engine("postgresql://postgres:1234@localhost:5432/chatbot", echo = False)
		
		# Heroku
    engine = create_engine("postgresql://xnrniyjhurkuos:b0d752cc9e29106fb8c4b1f7cd39c985a5a23bb67a35d8c365a6175355e9bf13@ec2-50-19-255-190.compute-1.amazonaws.com:5432/dashvvhprslttt", echo = False)

    engine.connect()
    engine.execute("""
        CREATE TABLE IF NOT EXISTS area(
            주택명 text,
            주택상세구분명 text,
            공급위치 text,
            모집공고일 text,
            청약접수시작일 text,
            청약접수종료일 text,
            당첨자발표일 text,
            홈페이지주소 text
        );"""
    )
    data = pd.read_csv('data/area.csv')
    print(data)
    data.to_sql(name='area', con=engine, schema = 'public', if_exists='replace', index=False)

app = Flask(__name__)

@app.route("/")
def index():
    db_create()
    return "Hello World!"



if __name__ == "__main__":
    db_create()
    app.run()