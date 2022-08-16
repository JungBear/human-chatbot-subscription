from flask import Flask
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
engine = create_engine("postgresql://xnrniyjhurkuos:b0d752cc9e29106fb8c4b1f7cd39c985a5a23bb67a35d8c365a6175355e9bf13@ec2-50-19-255-190.compute-1.amazonaws.com:5432/dashvvhprslttt", echo = False)

engine.connect()

def db_create():
    engine.execute("""
        CREATE TABLE IF NOT EXISTS announcement(
            Name TEXT NOT NULL,
            Division TEXT NOT NULL,
            Location TEXT NOT NULL,
            Notice_date TEXT NOT NULL,
            Start_day TEXT NOT NULL,
            End_day TEXT NOT NULL,
            release_date TEXT NOT NULL,
            Rink TEXT NOT NULL
        );"""
    )
    data = pd.read_csv('data/area.csv')
    print(data)
    data.to_sql(name='announcement', con=engine, schema = 'public', if_exists='replace', index=False)


def db_select(loc):
    # loc = "\'loc'"
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
    return df


app = Flask(__name__)

@app.route("/")
def index():
    # db_create()
    return "Hello World!"


if __name__ == "__main__":
    db_create()
    # db_select()
 
    app.run()