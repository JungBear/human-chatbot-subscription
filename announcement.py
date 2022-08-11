import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import os
import psycopg2

def DATABASE():
    DATABASE_URL = os.environ['postgresql://xnrniyjhurkuos:b0d752cc9e29106fb8c4b1f7cd39c985a5a23bb67a35d8c365a6175355e9bf13@ec2-50-19-255-190.compute-1.amazonaws.com:5432/dashvvhprslttt']
    conn = psycopg2.connect(DATABASE_URL, sslmode = 'require')


def input_region(region):
    result = conn[conn['공급위치'].str.contains(region)]
    return result


if __name__ == '__main__':
    region = str(input('지역을 입력해주세요 :'))
    result = input_region(region)
    print(result)
