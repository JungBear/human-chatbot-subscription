import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import os
import psycopg2

import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import os
import psycopg2


try:
    conn = psycopg2.connect(host="ec2-50-19-255-190.compute-1.amazonaws.com", dbname="dashvvhprslttt", user="xnrniyjhurkuos", password="b0d752cc9e29106fb8c4b1f7cd39c985a5a23bb67a35d8c365a6175355e9bf13")
    # heroku 
    cur = conn.cursor()
    cur.execute("select * from public.score ;")
    rows = cur.fetchall() 
    # list 타입
    # DataFrame으로 만들어주기
    df1 = pd.DataFrame(rows, columns = ['Item', 'Division', 'Score', 'Id'])
    print(rows)

except psycopg2.DatabaseError as db_err:
    print(db_err)


def score(num):
    df1[df1['Id'] == num]
    sql = "SELECT * FROM public.score where Item = '무주택기간' & Id = %s"
    cur.execute("SELECT * FROM public.score ")
    score = cur.fetchall()
    
    print(score)


if __name__ == '__main__':
    num = str(input('숫자를 입력해주세요 :'))
    result = score(num)
    #print(score)



