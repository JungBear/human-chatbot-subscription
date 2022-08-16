# -*- coding: utf-8 -*-
from unittest import result
from flask import Flask, jsonify, request
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import psycopg2
from announcement import df, input_region

app = Flask(__name__)

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

if __name__ == '__main__':
    announcement_output()

