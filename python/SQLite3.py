import sqlite3                 # sqlite3는 파이썬 내장 함수이므로, 따로 설치할 필요없음

### sqlite를 사용하는 이유와 특징
# https://www.itworld.co.kr/news/117213

print(sqlite3.version)         # sqlite의 모듈 버젼 확인
print(sqlite3.sqlite_version)  # sqlite 버젼 확인

### 커서 및 db 생성
con = sqlite3.connect(r'C:\Users\com\kospi.db')    ## 해당 디렉터리에 커서 연결,  해당 db가 없다면 생성하면서 커서 연결
cursor = con.cursor()                              ## 커서 객체화 하기
print(type(con))

### 오라클(cx_oracle)과의 차이 .   오라클과는 사뭇다르다.
# conn = cx_Oracle.connect('AA/ora1111@10.93.72.21:1738/ORCL')  ## 계정 접속


### create table    :  db에 테이블이 진짜 생성되므로, 2번째 실행시 테이블 중복되어 생성안됨
# cursor.execute('CREATE TABLE kakao(Date text, Open int, High int, Low int, Closing int, Volumn int)')  # ()은 컬럼명과 컬럼 데이터 타입 순


### Insert
cursor.execute("INSERT INTO kakao VALUES('16.06.03', 97000, 98600, 96900, 98000, 321405)")
cursor.execute("INSERT INTO kakao VALUES('16.06.02', 99000, 99300, 96300, 97500, 556790)")

### commit
con.commit()


### Select  및  cursor 활용
cursor.execute('SELECT * FROM kakao')

for i in cursor:
    print(i)

### fetchone()
cursor.fetchone()   # : 로우 단위(레코드 단위)로 데이터 읽어오기,  결과값:   ('16.06.03', 97000, 98600, 96900, 98000, 321405)
cursor.fetchone()   # : 로우 단위(레코드 단위)로 데이터 읽어오기,  결과값:   ('16.06.02', 99000, 99300, 96300, 97500, 556790)


### fetchall()
cursor.fetchone()  # : 한번에 모든 로우 읽어오기,   결과값:   ('16.06.03', 97000, 98600, 96900, 98000, 321405)
                   #                                     ('16.06.02', 99000, 99300, 96300, 97500, 556790)


### 커서 닫기
con.close()


#####  데이터베이스 브라우저  #####       : 데이터베이스에 저장된 데이터를 효과적으로 보여주는 프로그램
# 설치: (http://sqlitebrowser.org/)
# 설치시, sqlcipher도 같이 설치됨
# SQLCipher는 SQLite 데이터베이스 파일에 CBC 모드의 256비트 AES 암호화를 추가함 - 암호화는 OpenSSL libcrypto 라이브러리 사용
# 높은 보안성과 호환성을 보장하는 대신 약 7MB정도 .apk파일이 커지며, 약 5% 정도의 성능저하 발생











#####   DataFrame 객체를 SQLite DB에 저장하기  #####
import sqlite3
import pandas as pd

raw_data = {'col0': [1, 2, 3, 4], 'col1': [10, 20, 30, 40], 'col2':[100, 200, 300, 400]}
df = pd.DataFrame(raw_data)


con = sqlite3.connect(r'c:\Users\com\kospi_new.db')

# (중요) 아래 to_sql 활용시, 커서를 이용하지 않으므로,
# (중요) cursor = con.cursor()로 커서 생성 필요없음
# cursor = con.cursor()


df.to_sql('test', con, if_exists= 'replace')  ## 데이터 프레임을 (to_sql을 통해) 데이터베이스로 저장,
                                              ## 첫번쨰 인자 : 'test'라는 테이블로 생성,    두번째 인자 :  접속 객체

#  < to_sql 알아보기 >
#  DataFrame.to_sql(name, con, flavor='sqlite', schema=None, if_exists='fail',
#                   index=True, index_label=None, chunksize=None, dtype=None)
#
# name	: SQL 테이블 이름으로 파이썬 문자열로 형태로 나타낸다.
# con	: Cursor 객체
# flavor: 사용한 DBMS를 지정할 수 있는데 'sqlite' 또는 'mysql'을 사용할 수 있다. 기본값은 'sqlite'이다.
# schema : Schema를 지정할 수 있는데 기본값은 None이다.
# if_exists	: 데이터베이스에 테이블이 존재할 때 수행 동작을 지정한다. 'fail', 'replace', 'append' 중 하나를 사용할 수 있는데
#             기본값은 'fail'이다. 'fail'은 데이터베이스에 테이블이 있다면 아무 동작도 수행하지 않는다.
#             'replace'는 테이블이 존재하면 기존 테이블을 삭제하고 새로 테이블을 생성한 후 데이터를 삽입한다.
#             'append'는 테이블이 존재하면 데이터만을 추가한다.
# index :  DataFrame의 index를 데이터베이스에 칼럼으로 추가할지에 대한 여부를 지정한다. 기본값은 True이다.
# index_label :	인덱스 칼럼에 대한 라벨을 지정할 수 있다. 기본값은 None이다.
# chunksize : 한 번에 로우의 크기를 정숫값으로 지정할 수 있다. 기본값은 None으로 DataFrame 내의 모든 로우가 한 번에 써진다.
# dtype : 칼럼에 대한 SQL 타입을 파이썬 딕셔너리로 넘겨줄 수 있다.



df = pd.read_sql("SELECT * FROM kakao", con, index_col=None)
## 첫번쨰 인자 : SQL 구문
## 두번째 인자 : 접속 객체
##  index_col는 DataFrame 객체에서 인덱스로 사용될 칼럼을 지정. 기본값은 None. None을 입력하면  0부터 차례로 정수 인덱스 할당

print(df)









#####  Pandas를 이용한 주가 데이터 저장  #####


import pandas as pd
import pandas_datareader.data as web
import datetime
import sqlite3

start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2016, 6, 12)
df = web.DataReader("078930.KS", "yahoo", start, end)  ## GS 종목 데이터를 데이터프레임 객체 df에 저장
print(df)

con = sqlite3.connect(r'c:\Users\com\kospi_new.db')
df.to_sql('078930', con, if_exists='replace')          ## df 데이터를 데이터 베이스에 저장

readed_df = pd.read_sql("SELECT * FROM '078930'", con, index_col = 'Date') # 인덱스 컬럼 'Date'로 지정 후 다시 읽어오기