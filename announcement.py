import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import os
import psycopg2


try:
    conn = psycopg2.connect(host="ec2-50-19-255-190.compute-1.amazonaws.com", dbname="dashvvhprslttt", user="xnrniyjhurkuos", password="b0d752cc9e29106fb8c4b1f7cd39c985a5a23bb67a35d8c365a6175355e9bf13")
    # heroku에 배포되어 있는 데이터베이스에 접속하기
    cur = conn.cursor()
    # cursor = 임시 객체생성
    # 생성된 임시객체를 cur에 저장
    cur.execute("select * from public.announcement;")
    # sql문장을 실행할 수 있게 해주는 메서드
    rows = cur.fetchall() 
    # 데이터내용 전부 불러서 rows에 입력
    # list 타입
    df = pd.DataFrame(rows, columns = ['Name','Division','Location','Notice_date','Start_day','End_day','release_date','Rink'])
    # DataFrame으로 만들어주기
    # 컬럼명을 지정

except psycopg2.DatabaseError as db_err:
    print(db_err)
    # 접속을 못했을때 에러 출력

def input_region(region):
    result = df[df['Location'].str.contains(region)]
    # 입력받은 값 df의 Location에 
    return result


if __name__ == '__main__':
    region = str(input('지역을 입력해주세요 :'))
    result = input_region(region)
    print(result)
