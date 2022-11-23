import pandas as pd

## 데이터 읽어오기
# read_csv
file_url = "http://bit.ly/ds01-weight-history"
data=pd.read_csv(file_url, index_col = '회차')   # index_col = '회차' 회차를 index로 읽음
titanic=pd.read_csv(r'C:\Users\6509504\Desktop\data analysis train/train.csv.csv',  encoding = 'utf8')

# sheet를 골라 읽어오기 (없으면 기본(default)시트로 읽어옴)
titanic = pd.read_excel(excel_file3, sheet_name = '개정 이력' )

## 데이터 쓰기
titanic.to_excel("1.xlsx", index=False)

# dataframe 통째로 복사
titanic = train.copy() #copy를 쓰는 이유는 혹시나 age_fill과 age과 완전히 연동될 문제가 있기떄문에

# DataFrame 직접 생성
a= [1,2,3]
b=[4,5,6]
c=[7,8,9]
pd_123 = pd.DataFrame([a,b,c])
pd_12 =  pd.DataFrame({'a':a, 'b':b, 'c':c})  ###  DataFrame 지정 방식에 따라 원소 배열이 다르다 !
print(pd_123, '\n')
print(pd_12, )
# 실행결과 >>
#     0  1  2
#  0  1  2  3
#  1  4  5  6
#  2  7  8  9
#
#     a  b  c
#  0  1  4  7
#  1  2  5  8
#  2  3  6  9


##### dict.items()로 dataframe 만들기
dict = {}
dict['a']=1
dict['b']=2
dict['c']=2

print(dict)          # {'a': 1, 'b': 2, 'c': 2}
print(dict.items())  # dict_items([('a', 1), ('b', 2), ('c', 2)])

import pandas as pd
a = pd.DataFrame(dict.items(), columns=['aa', 'n'])
print(a)
#   aa  n
# 0  a  1
# 1  b  2
# 2  c  2



# dataframe인덱스 확인     .index
print(data.index)

# dataframe 컬럼 확인
print(data.columns)


# dataframe 행렬 확인
print(data.shape)


# 값의 종류 보여주기 - unique, nunique
data['지점'].unique()   # 증복제거한 값, 값의 종류만 보여줌 - 순서는 많은 순서부터 3 > 1 > 2 순서로 많은것
# 실행결과 : array(['강남', '여의도', '강남구'], dtype=object)
data['지점'].nunique()  ##종류의 개수
# 실행결과 : 3


# 요소별 상관계수 출력
train.corr() ## 각 요소들의 상관계수를 보여줌 /  +: 비례관계, -: 반비례관계   /  0.3 이상이면 비례 관계가 높다고 판단


# 값의 종류별개수 보여주기
data['담당'].value_counts()     # 종류별 개수 출력
data['담당'].value_counts().sort_index() # 종류별 개수 출력하고 이를 정렬하여 출력
train['Pclass'].value_counts(normalize=True)   ## 비율로 변환하여 출력


# index reset 하기   -  reset_index()
SEQ_sr = coding_raw_df[SEQ_col][SEQ_row+3:SEQ_row+3+SEQ_cnt].reset_index(drop = True)   # 기존 인덱스를 열로 추가하지 않기
SEQ_sr = coding_raw_df[SEQ_col][SEQ_row+3:SEQ_row+3+SEQ_cnt].reset_index()   # 기존 인덱스를 열로 추가함



# 타입 정보 확인하기
train.info()   ## 타입 정보, 컬럼별 non-null count, Dtype 출력


# 통계값/통계량 확인하기
data.describe()   #count, mean, std, max 등
data["몸무게"].describe()
pd.pivot_table(data, index="지점", values= "몸무게")  # 지점을 index 열로  몸무게의 평균값 출력 (default 평균)
pd.pivot_table(data, index=["지점", "담당"], values= ["몸무게", "측정일"], aggfunc = ["mean", "sum"]) # aggfunc : 사용할 통계 정의
data.count() # 컬럼별 행의 개수 출력
data['담당'].count() # '담당' 열의 행의 개수 출력


# 최빈값 출력 : mode()
a_df = pd.DataFrame({'a':[1,2,3,1,2,3]})
a_df.mode() ## 최빈값이 복수일때는 모두 출력됨 (1,2,3 값을 series로 출력)

b_df = pd.DataFrame({'a':[1,2,3,1,2,3,1]})
b_df.mode() ## 최빈값이 한개일때는 1개만 출력됨 (1 값을 series로 출력)
b_df.mode()[0]  ## 최빈값만 출력하고 싶을때



# 정규화 수행
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {
    'A': np.random.choice(10000, 1000),
    'B': np.random.choice(1000000, 1000),
    'C': np.random.choice(100, 1000),
    'D': np.random.choice(10, 1000)
}

df = pd.DataFrame(data)
normalization_df = (df - df.mean())/df.std()

# df.mean() 실행시 출력:
# A      4912.337
# B    508322.860
# C        51.005
# D         4.431
# dtype: float64



# data 변경/바꾸기 replace
data["지점"]=data["지점"].replace("강남","강남구")
mapper = {0 : "Perish", 1 : "Survived"}
train["Survived{char2}"] = train['Survived'].replace(mapper)


# 빈칸 행 찾기  isnull
print(data[data["몸무게.prev"].isnull()])
train['Age'].isnull().sum()  # null 값 개수 확인 , isnull에서 True로 출력되는 행 177개 합산 (True는 1로 취급, False는 0 취급)


# 빈값 아닌 행 찾기
print(data[data["몸무게.prev"].notnull()])


# 빈칸 값 채우기    fillna
data["몸무게"]=data["몸무게"].fillna(75.8)


# 빈칸 행 삭제하기
train['Age'].dropna() #null값 행 삭제  , 889행 삭제됨


# 행을 한칸씩 올려/내려 출력하기   - shift
data["몸무게.prev"]= data["몸무게"].shift(+1)
data["몸무게.next"]= data["몸무게"].shift(-1)


# datetime 타입 활용
data["측정일"]=pd.to_datetime(data["측정일"]) # datetime 타입으로 바꾸기
print(data["측정일"].dtype)     # datetime 출력
print(type(data["측정일"]))     # series라고 출력
print(data["측정일"].dt.year)
print(data["측정일"].dt.month)
print(data["측정일"].dt.day)
print(data["측정일"].dt.hour)
print(data["측정일"].dt.minute)
print(data["측정일"].dt.second)
print(data["측정일"].dt.weekday) # -> 날짜를 요일로 변경시킴 (2021-01-01 -> 1(화요일))


# 데이터의 원소 타입 확인하기
print(data["측정일"].dtype)     # datetime 출력


# 데이터 원소 타입 바꾸기    to_datetime(), astype()
data["측정일"]=pd.to_datetime(data["측정일"])  # datetime으로
data["측정일"]=pd.to_numeric(data["측정일"])   # number 타입으로
train['year-month(str)']=train["datetime-year"].astype(str)  # astype을 활용하여 str 타입으로 변경 (pandas에서만 가능)


# select_dtypes을 활용하여 데이터 원소 타입 별로 추출하기
categorical_columns = data.select_dtypes(include = ['object']).columns  # object 타입만 추출
numerical_columns = data.drop(columns = ['y']).select_dtypes(include = ['int', 'float']).columns # int, float 타입만 추출

# .str 활용하기
x=pd.DataFrame({'a':['ax','b'],'b': ['axe', 'tool']})
print(x['a'].str.replace('a','b'), '\n') # str로써 replce 적용되므로 바뀜   ax -> bx
print(x['a'].replace('a','b'), '\n') # series로써 적용되므로 'a'라는 데이터가 없어 안바뀜 (똑같아야함)
print(ab.str.replace('a','b'), '\n')    ## 에러 발생, DateFrame은 .str 적용안됨, series만 .str 적용가능
consensusDataFrame['YYMM'] =  consensusDataFrame['YYMM'].str.strip().str[:-3]   ## 문자열 slice하기
consensusDataFrame['YYMM'] =  consensusDataFrame['YYMM'].slice(start=0, stop=5, step=3)


## dataframe에서 원하는 행, 렬 추출하기
data.head()    # 상위 10개 행 출력 - default 10개
data.head(5)   # 상위 5개 행 출력
data.tail()    # 하위 10개 행 출력 - default 10개


# dataframe의 행/렬 추출,    loc: index 컬럼의 원소 값, iloc: index 값
data.loc[{1,3,7}]     # 회차(인덱스) 컬럼에서 값이 1,3,7인 행 출력
print(data.loc[1:5])  # 회차(인덱스) 컬럼에서 값이 1~5인 행 출력
print(data.iloc[0:7]) # 인덱스 값이 0~7인 행 출력

print(data.loc[[1,3], ["이름", "측정일", "몸무게"]])  # 행, 렬 조건 출력
print(data.loc[1:7, ["이름", "측정일", "몸무게"]])   # 행, 렬 조건 출력


# 조건에 따른 dataframe 출력
print(data[data['담당']=="김지수"])  # 담당 열에서 김지수 이름 가진 행 모두 출력
print(data[data['몸무게']>75])
print(data[data["담당"].isin(["김지수", "최재우"])])  # 담당 열에서 김지수, 최재우 존재시 출력
print(data[data["담당"].str.contains("김")])  # 담당 열에서 '김' 포함시 출력
print(data[(data["담당"]=="김지수") & (data["몸무게"] > 75.5)])


pclass_1 = train['Pclass'] == 1
fare_over_200 = train['Fare'] >200
print(pclass_1 & fare_over_200)

# loc를 이용한 조건에 따른 dataframe 출력
data.loc[data["담당"] == "김지수", "몸무게"] # 행: 담당 열에서 '김지수'를 가진 행  & 열: '몸무게'열  출력
data.loc[data["담당"] == "김지수", ["몸무게", "지점"]] # 행: 담당 열에서 '김지수'를 가진 행  & 열: '몸무게'+'지점' 열  출력



# column 열 만들기
item_names = ["접수번호", "사업연도", "고유번호", "보고서코드", '계정 ID', "계정명", "계정상세", "개별연결구분", "개별연결명", "재무제표구분",
              "재무제표명", "당기명", "당기일자", "당기금액", "당기누적금액", "전기명",
              "전기금액", '전기명(분/반기)', '전기금액(분/반기)', "전기누적금액", "전전기명", "전전기금액", "계정과목정렬순서"]
df = pd.DataFrame(columns=item_names)


# column 열 추가
data.loc[data["몸무게"]>75.8, "상태1"]  = "과체중"   # 상태1 열 추가
data.loc[data["몸무게"]<=75.8, "상태1"]  = "정상"    # 상태1 열 추가

# column 열 삭제
data=data.drop(columns=["상태","상태1"])  # 상태, 상태1 열 삭제
data.drop("상태1", axis = "columns")     # 상태1 열 삭제

# row 행 삭제
data.drop(1, axis = "index")

# column 명 바꾸기 (열 이름 바꾸기)
train=train.rename(columns={"date": "Date", "Rank": "RANK"}) # date를 DATE로, Rank를 RANK로 변경

# series columns 명 바꾸기
data_sr = data_sr.rename('weight')
rev_data = rev_data.rename( columns= {0 :'veh_num'})   ## INDEX를 이름으로 변경

# 원소 값별 column 자동 생성 - ont hot encoding
# data['측정일 dt']= pd.to_datetime(data['측정일'])
# data['측정일 day']=data['측정일 dt'].dt.weekday
a_dum = pd.get_dummies(data['측정일 day'], prefix='측정일 day')   ## prefix로 구분자를 추가함 (prefix 없으면 값으로만 컬럼 이름 지정)
a_dum = pd.get_dummies(data['측정일 day'], prefix='측정일 day', prefix_sep='')   ## prefix로 구분자를 ''로 지정 (default = '_')

data = pd.read_csv('mercedes_test.csv')
data.dtypes   # 결과값 : float, object, int 등
data = pd.get_dummies(data)   ## get_dumiies는 알아서 카테고릭 타입 혹은 object 타입에 대해서만 원핫인코딩을 진행하고, 다시 합쳐줌 !!!!!!!!!
data.dtypes  # 결과값 : int, float

# 측정일 day의 원소값 대로 새로운 dataframe 'a_dum' 생성
# a_dum.columns = ['측정일 day_0', '측정일 day_1', '측정일 day_2', '측정일 day_3', '측정일 day_4', '측정일 day_5', '측정일 day_6']

# DataFrame 끼리 합치기
# - concat, merge, join

# concat
a_dum = pd.get_dummies(data['측정일 day'], prefix='측정일 day')
data = pd.concat([data,a_dum])               # 행 기준으로 합치기 -> 행이 늘어남
data = pd.concat([data,a_dum], axis=1)       # 열 기준으로 합치기 -> 열이 늘어남  (default : 행 기준)
t = pd.concat([pd.get_dummies(a['N']), pd.get_dummies(a['HOW']), pd.get_dummies(a['VOL']],  axis = 1)

# merge        : https://yganalyst.github.io/data_handling/Pd_12/
merge_inner = pd.merge(df1, df2)   # 두 데이터프레임 중에서 열에 공통의 값이 존재하면, 그 열을 기준으로 inner join 실시
merge_outer = pd.merge(df1,df2, how='outer',on='id')   # on='id'를 통해 기준 열을 정해줌 -> 없으면 공통의 값을 통해 스스로 찾음
                                                       # how='outer'를 통해 inner/outer join 여부 결정
merge_left = pd.merge(df1,df2, how='left', left_on='stock_name', right_on='name')
# 양쪽에 각각 다른 columns을 기준으로 하고 싶다면, left_on='stock_name', right_on='name' 사용
# left join의 경우, df1을 기준으로 하여, df1에는 없는 df2의 성분은 버림

# join         : https://yganalyst.github.io/data_handling/Pd_12/
df1.join(df2) #default 값이 how = 'left'이다. df1을 기준으로 하여, df1에는 없는 df2의 성분은 버림


# apply 사용법  
# 기본형태 : df.apply(func, axis=0, raw=False, result_type=None, args=(), **kwds)
# axis : 0이면 index따라 입력, 1이면 column따라 입력
# args : 함수에 추가로 필요한 배열 또는 series를 tuple로 입력
# kwds : 함수에 추가로 필요한 dict의 key값을 입력
# 나머지는 쥬피터에서 alt + tab 눌러서 찾기

import numpy as np
def band(w):
    if pd.isnull(w):
        return "n"
    else:
        return 1

a=pd.DataFrame()
a["열"] =[1,2,3,None, np.nan,7,8]

b=a["열"].apply(band)
print(b)  # None, np.nan 일때 'n' 출력  그외 1 출력


# apply 사용법 2
def band_weight(weight):
    # weight 변수에 NaN이 들어왔으면 별도의 처리를 하지 않고 NaN으로 반환합니다.
    if pd.isnull(weight):
        return np.nan              ##pandas에서는 none 또는 np.nan으로 null값 입력

    # weight 변수에 있는 값이 75.5 kg 미만이면 '초과'라는 값을 반환합니다.
    if weight < 75.5:
        return '초과'
    # weight 변수에 있는 값이 75.5 kg 이상이고 76.0 kg 이하면 '달성'이라는 값을 반환합니다.
    elif weight >= 75.5 and weight < 76.0:
        return '달성'
    # 모든 조건해 해당하지 않으면 '미달'이라는 값을 반환합니다.
    else:
        return '미달'

# Name 컬럼에 apply를 실행합니다. 인자로는 band_weight라는 함수를 집어넣습니다.
# 이렇게 하면 전체 목표 데이터 값에 대해 band_weight를 실행한 뒤 그 결과를 반환합니다.
# 반환한 결과를 목표라는 이름의 새로운 컬럼에 집어넣습니다.
data["목표"] = data["몸무게"].apply(band_weight)

# 이름(Name)과 호칭(Title) 컬럼을 출력하여 두 가지를 비교합니다.
data[["몸무게", "목표"]]


# apply 사용법 3-1  : args 사용
def bin_weather(weather, good_list):
    if weather in good_list:
        return "good"
    else : 
        return "bad"
    
a=train['weather'].apply(bin_weather,args= ([1,2],)) # tuple 내 list 형태의 원소 1개를 전달함)
                                                     # args는 매개변수를 크기/개수 자유롭게 튜플(tuple) 형태로 넘겨줌 - memo chapter 확인                                                     
a.value_counts()


# apply 사용법 3-2  : args 사용
def bin_weather(weather, good_list, bad_list):  
    if weather in good_list:
        return "good"
    elif weather in bad_list : 
        return "bad"
    else: 
        return None

a=train['weather'].apply(bin_weather,args= ([1,2],[3,4])) ## tuple 내 list 형태의 원소 2개를 전달함)
a.value_counts()


# apply 사용법 4  : axis = 1 사용(row별 입력) 
## : 데이터 프레임 내에 여러 인자를 apply 적용하고 싶은 경우
def get_discomfort_index(row): # 한 행을 통째로 입력 받아, 각 컬럼 인자를 활용
    humidity = row['humidity']
    temp = row['temp']
    windspeed = row['windspeed']
    
    return humidity*temp+windspeed
train.apply(get_discomfort_index, axis=1) 


# apply 사용법 5  : axis = 0 사용(컬럼별 입력) 
# train에서 컬럼별로 함수에 입력하여, 해당 컬럼의 모든 원소를 모두 문자로 더하여 리턴함
# ex) train['weather']의 원소 1,1,2,3,4,1,0를 모두 더하여 1123410으로 출력
def bin_weather(weather):
    k=0
    for i in range(len(weather)):
         k = str(k)+str(weather[i])
               
    return k
        
a=train.apply(bin_weather, axis=0)  
print(a['datetime'])



# DATAFRAME 끼리 비교 (데이터프레임끼리 비교)   +    np. where 와의 차이점
s = a['VOL'].where(a['VOL']=='E', 'OK')  # Series객체.where(Series객체에 대한 조건문, 거짓 값에 대한 대체 값)  -> 인자 2개
s = a['VOL'].where(a['VOL'].eq(a['HOW']), None)  # Series끼리 열 비교
s = a.loc[1].where(a.loc[1].eq(a.loc[2]), None)  # Series를 행 비교
# s = np.where(a['VOL'].eq(a['EW']), 'OK', '')  #  np.where(배열에 대한 조건문, 참일때 값, 거짓일때 값)   -> 인자 3개

# 예시
df1 = pd.DataFrame({'a': [1,2,3,4,5] , 'b': [ 5,6,7,8,9], 'c' : [100,200,300,400,500]})
df2 = pd.DataFrame({'a': [1,2,3,4,5,6] ,  'c' : [100,200,300,400,500,600]})

tt = df1.loc[4].where(df1.loc[4].eq(df2.loc[4]), None) ## 정상 동작함 (컬럼 네임을 기준으로 비교하므로, 컬럼 개수가 안맞아도 동작함)
print(tt)



# DATAFRAME에서 원하는 값 찾기     isin()
print(df1[df1.isin([3])])   # isin() 사용

# DATAFRAME에서 원하는 값 찾기     np.argwhere()
t = np.array(df1)   # dataframe을 array로 변경  1
print(np.argwhere(t == 7), type(np.argwhere(t == 7))) # 결과값 [[2 1]],  <class 'numpy.ndarray'>
c = np.argwhere(t == 7)
print(c[0][0])  # 결과값 2
print(np.argwhere(t == 5))                    # 결과값이 2개일 경우, 리스트로  [[0 1] [4 0]] 모두 서치가능
print(len(comb))                              # 결과값 2,   2개 모두 서치


# dataframe을 array로 변경 2
t.values   # 결과값 : array([1, 2, 3, 5, 6, 7])


# DATAFRAME에서 원하는 값 찾기     get()
df1 = pd.DataFrame({'a': [1,2,3,4,5] , 'b': [ 5,6,7,8,9], 'c' : ['100','200','300','400','500']})
print(df1['c'].get('100'))   ## 결과값 : None,  sereis에서 문자열은 get안됨   - get은 찾을 값이 없더라도, fail이 아닌 None을 반환
print(df1['a'].get(1))   ## 결과값 : 2,  sereis에서 숫자로 get 입력시, 인덱스로 활용됨
print(df1.get('a'))      ## 결과값 :  df1['a'] series 출력


# columns slice ( 컬럼 슬라이스 ) 하기 , 컬럼 자르기
coding_raw_df.loc[SEQ_row+3:SEQ_row+3+SEQ_cnt, nation_col_st:nation_col_end]  # 첫번째: 행 슬라이스 ,두번째: 열 슬라이스


# DATAFRAME 행/렬 바꾸기 (전치)   transpose()
df1 = df1.transpose()


# DATAFRAME 에서 값만 추출하기    item()
a = df[df['계정명'].isin(['기본주당이익(손실)'])]['당기금액'].item()






# groupby
titanic = pd.read_csv('titanic.csv')
print(titanic.groupby(['Sex','Pclass'])[['Survived', 'Fare']].mean()) ## 'Sex','Pclass' 별(입력 변수)로    'Survived', 'Fare'(결과 변수)에 대한 평균치를 출력함
print(titanic.groupby('Sex')[ 'Fare'].mean()) # Sex에 따른  Fare에 대한 평균치를 그룹별로 표현함 (남자 : 000, 여자 : 111)



## DATAFRAME에서 INDEX 값 반환받기
print (df.index[df['B'] == 19].tolist())    ## 19라는 값을 갖는 df의 row(index)를 리스트 형태로 반환
print (df.index[df['B'] == 19])  ## 19라는 값을 갖는 df의 row(index)를 시리즈 형태로 반환




### DataFrame과 Numpy-array 전체 print 보여주게하는 옵션
import sys
import numpy as np

np.set_printoptions(threshold=sys.maxsize)
pd.set_option('display.max_rows', None)
