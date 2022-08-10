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
        CREATE TABLE IF NOT EXISTS score(
            가점항목 TEXT,
            가점구분 TEXT,
            점수 BIGINT,
            입력값 BIGINT
        );"""
    )
    data = pd.read_csv('data/score.csv')
    print(data)
    data.to_sql(name='score', con=engine, schema = 'public', if_exists='replace', index=False)

app = Flask(__name__)

@app.route("/")
def index():
    db_create()
    return "Hello World!"



if __name__ == "__main__":
    db_create()
    app.run()