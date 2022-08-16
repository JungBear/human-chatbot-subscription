# -*- coding: utf-8 -*-
from unittest import result
from flask import Flask, jsonify, request
import os,sys, json
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import psycopg2
from announcement import input_region

app = Flask(__name__)

@app.route("/")
def hello():
    return "hellllllll123"

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

