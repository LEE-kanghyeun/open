import pandas as pd
at =r'C:\Users\com\Desktop\[교육]데이터 분석 교육_201106\data analysis train\1주차 교육 자료\train - train.csv.csv'
titanic=pd.read_csv(at, encoding = 'UTF-8')
titanic.head()
train = pd.read_csv(r'c:\Users\com\Desktop\[교육]데이터 분석 교육_201106\data analysis train\2주차 교육 자료 bike-sharing-demand\train.csv', encoding='UTF-8')
train['datetime'] = pd.to_datetime(train['datetime'])
train['year'] = train['datetime'].dt.year
train['month'] = train['datetime'].dt.month
train['day'] = train['datetime'].dt.day
train['hour'] = train['datetime'].dt.hour
train['minute'] = train['datetime'].dt.minute
train['second'] = train['datetime'].dt.second
train.head()



########################  seaborn  ###########################
##### 자료 준비 ######

pd.pivot_table(titanic, index="Embarked", values="Fare")  # pandas 기능의 피봇테이블 활용
pd.pivot_table(titanic, index="Embarked", values=["Fare", "Survived"])

##### seaborn ######
import seaborn as sns
sns.countplot(data=titanic, x="Pclass", hue="Survived" )  # countplot 그래프 (1변수)
sns.barplot(data=titanic, x="Pclass", y="Fare", hue="Survived") # barplot 그래프 (2변수)
sns.pointplot(data=titanic, x="Pclass", y="Fare", hue="Survived") # pointplot 그래프 (꺽은선 그래프)
sns.lmplot(data=titanic, x="Age", y="Fare", hue="Survived", fit_reg=False)  # lmplot 그래프 (점 그래프)
sns.distplot(titanic["Fare"]) # distplot 그래프 (분포그래프, 분포함수)
sns.heatmap(data = train.corr())  # 히트맵 출력 (색깔로 상관관계 표현) # train.corr() 은 인자별 상관관계 출력
sns.boxplot(data = split_data, y = 'BedroomAbvGr'  ,ax=ax1)
sns.swarmplot(x='class', y='age', data=titanic, ax=ax2, hue='sex')  # 이산형 변수의 분포 - 데이터 분산 고려 (중복 X)
sns.stripplot(x='class', y='age', data=titanic, ax=ax1)   # 이산형 변수의 분포 - 데이터 분산 미고려

# 그래프 겹쳐서 한곳에 그리기
sns.pointplot(data=train, x='month', y='count' ,color='brown')  # 색깔 정하기
sns.pointplot(data=train, x='month', y='casual' , color = 'red') # 색깔 정하기
sns.pointplot(data=train, x='month', y='registered')


# -> 그래프 크기 정하려면 matplotlib 사용 필요
#    figure.set_size_inches(18, 8)  : 그래프 크기 정하기






########################  matplotlib  ###########################




########## Scatter Plot 활용  + Plot에 텍스트 삽입하기 ##########

# https://towardsdatascience.com/how-to-add-text-labels-to-scatterplot-in-matplotlib-seaborn-ec5df6afed7a  ## plot에 텍스트 넣기
# https://codetorial.net/matplotlib/add_text.html ## plot에 텍스트 넣기

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
plt.scatter(TP_MDS_df[0], TP_MDS_df[1], s = 150 )

for i in TP_MDS_df.index:
  plt.text(TP_MDS_df[0][i], TP_MDS_df[1][i], s = i, fontdict= { 'size' : 16}  )

plt.show()





########## 여러 그래프 동시에 출력하기 (subplot) ###########


import matplotlib.pyplot as plt
##### 자료 준비 ######  : 위 seaborn꺼 사용

### 그래프 그리기 시작 ###
plt.subplots(nrows=3, ncols=2)   # 4 X 3 행렬 모양의 12개의 subplot을 만듬

#subplot에 각 그래프 지정하기
figure, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(nrows=2, ncols=3)

figure.set_size_inches(18, 8)  # 그래프 크기 정하기

sns.barplot(data=train, x='year', y='count', ax=ax1)
sns.barplot(data=train, x='month', y='count', ax=ax2)
sns.barplot(data=train, x='day', y='count', ax=ax3)
sns.barplot(data=train, x='hour', y='count', ax=ax4)
sns.barplot(data=train, x='minute', y='count', ax=ax5)
sns.barplot(data=train, x='second', y='count', ax=ax6)




############ 여러 그래프를 자동으로 표현하기 ############

import seaborn as sns

import matplotlib.pyplot as plt


figure, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8),
         (ax9, ax10, ax11, ax12),(ax13, ax14, ax15, ax16),
         (ax17, ax18, ax19, ax20),(ax21, ax22, ax23, ax24),
         (ax25, ax26, ax27, ax28)) = \
plt.subplots(nrows= 7, ncols=4)

temp = raw_data.drop(columns = ['ID'])

figure.set_size_inches(50,40)

for i,v in enumerate(temp.columns[0:28]):
  a = 'ax'+str(i+1)
  sns.distplot(temp[v], ax= globals()[a])
  plt.title(v)




########## 여러 그래프 동시에 출력하기 (subplot) ###########

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

figure, ax = plt.subplots(7, 4, figsize=(18, 12))

# #subplot에 각 그래프 지정하기
# figure, ((ax1, ax2, ax3, ax4), (ax5, ax6,ax7, ax8)
# #         , (ax9, ax10,ax11, ax12), (ax13, ax14,ax15, ax16)
# #         , (ax17, ax18,ax19, ax20), (ax21, ax22,ax23, ax24), (ax25, ax26,ax27, ax28)
#         ) = plt.subplots(nrows=2, ncols=4)

figure.set_size_inches(50, 40)

for i in range(28):
    x = np.random.normal(size=100) * 1000
    y = np.random.normal(size=100) * 1000

    plt.subplot(7, 4, i + 1)
    plt.scatter(x, y, s=150)

plt.show()






########### 여러 그래프 출력하기 (add_subplot) ###########

import numpy as np
import matplotlib.pyplot as plt



x = np.arange(0.0, 2 * np.pi, 0.1)    # pi 는 파이
sin_y = np.sin(x)
cos_y = np.cos(x)

fig = plt.figure()               ##
ax1 = fig.add_subplot(2,1,1)     ## 2 x 1 행렬에서 1번째 subplot
ax2 = fig.add_subplot(2,1,2)     ## 2 x 1 행렬에서 2번째 subplot

ax1.plot(x, sin_y, 'b--')       ## 색상 : b(블루)   +   선(마커) 패턴 : --(대시 라인)
ax2.plot(x, cos_y, 'rs')        ## 색상 : r(레드)   +   선(마커) 패턴 : s(사각형)

## 색상 ##
# b	blue(파란색)
# g	green(녹색)
# r	red(빨간색)
# c	cyan(청록색)
# m	magenta(마젠타색)
# y	yellow(노란색)
# k	black(검은색)
# w	white(흰색)

## 마커 ##
# o	circle(원)
# v	triangle_down(역 삼각형)
# ^	triangle_up(삼각형)
# s	square(네모)
# +	plus(플러스)
# .	point(점)


ax1.set_xlabel('x')               ## 범례 표시
ax1.set_ylabel('sin(x)')          ## 범례 표시

ax2.set_xlabel('x')              ## 범례 표시
ax2.set_ylabel('cos(x)')         ## 범례 표시

plt.legend(loc='upper right')     ## 범례 위치 지정, 없으면 알아서 자동지정

plt.show()






########## 여러 그래프 출력하기 (subplot2grid 사용하기 :  subplot별 크기 따로 지정 가능) ##########
import matplotlib.pyplot as plt
import pandas_datareader.data as web
sk_hynix = web.DataReader("000660.KS", "yahoo")             ## 기간 지정안하면 최근 5년 출력

fig = plt.figure(figsize=(12, 8))   ## 전체 사이즈 지정

top_axes = plt.subplot2grid((4,4), (0,0), rowspan=3, colspan=4)
## 전체 figure를 4x4 ( (0,0)~(3,3) )로 봤을때, 0x0에서 시작하여 row측으로 3칸까지, column측으로 4칸까지 차지한다 즉 (0,0)~(2,3)
bottom_axes = plt.subplot2grid((4,4), (3,0), rowspan=1, colspan=4)
## 전체 figure를 4x4로 봤을때, 3x0에서 시작하여 row측으로 1칸까지, column측으로 4칸까지 차지한다 즉 (3,0)~(3,3)

bottom_axes.get_yaxis().get_major_formatter().set_scientific(False)  ## 아래측 거래량에서 큰 값이 발생해도, 오일러 상수의 지수형태로 표현되지 않도록 함 (엑셀처럼...)

top_axes.plot(sk_hynix.index, sk_hynix['Adj Close'], 'r.', label='Adjusted Close')
bottom_axes.plot(sk_hynix.index, sk_hynix['Volume'], 'b--')

plt.tight_layout()   # subplot들이 Figure 객체의 영역 내에서 자동으로 최대 크기로 출력되게 함 (여백 안남김)
plt.show()



##################### 3차원 시각화 ##########################
## https://jimmy-ai.tistory.com/30


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

x = np.arange(0, 10, 0.1)
y = np.sin(x)
z = np.cos(x)
ax.scatter(x, y, z)

###########################

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(TP_MDS_df[0], TP_MDS_df[1], TP_MDS_df[2], s = 150 )

for i in TP_MDS_df.index:
  ax.text(TP_MDS_df[0][i], TP_MDS_df[1][i], TP_MDS_df[2][i], s = i, fontdict= { 'size' : 16}  )

plt.show()




###########  candle (일봉)  차트  ############

import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import mpl_finance
import matplotlib.ticker as ticker
import pandas as pd
from matplotlib import font_manager, rc

start = datetime.datetime(2020, 12, 1)

end = datetime.datetime(2021, 2, 15)

skhynix = web.DataReader("000660.KS", "yahoo", start, end)
skhynix = skhynix[skhynix['Volume'] > 0]    ## 거래량이 없는 날은 (장이 쉬는 날) 제거함
# print(skhynix.tail(10))


# skhynix df index 값 변환하기,   2021-01-04 00:00:00 -> 2021-01-04
print(skhynix.index[0])  # index 값 2021-01-04 00:00:00로 시간없애는 편이 좋을듯
skhynix.index = skhynix.index.strftime('%Y-%m-%d')    ## Y : 2021,  y : 21 (두자리 연도), 변환 뒤에는 str 타입이 됨 (이전에는 date 타입)

# 월요일마다 skhynix df index에 (mon)이라고 표시해주기
new_index = list(skhynix.index)
date_sr = pd.to_datetime(skhynix.index)
for i,day in enumerate(date_sr):
    if day.dayofweek == 0:
        new_index[i] =  new_index[i] + '(mon)'
skhynix.index = new_index
print(skhynix.index)



### 캔들 차트 그래프 형태 지정 ###
# plt.xticks , plt.title, ticker.FixedLocator, ticker.FixedFormatter, mpl_finance.candlestick2_ohlc 활용

fig = plt.figure(figsize=(16, 12))   ## 그래프 지정시, 1순위로 써줘야함

#그래프에서 한글이 깨지는 것을 개선해줌 (아래 구문 없으면 한글 깨짐)
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False

# plt.rc('font', size=5)             ## 전체 글자 폰트 크기 일괄 변경 (타이틀, 라벨 등)
# plt.rc('xtick', labelsize = 7)       ## x축 폰트 크기만 변경    - 아래와 같이 xticks에서도 폰트 크기 변경 가능
# plt.rc('ytick', labelsize = 12)      ## y축 폰트 크기만 변경    - 아래와 같이 yticks에서도 폰트 크기 변경 가능
plt.xticks(rotation =60, size = 7)     ## rotation : 아래 x축 인덱스를 45도 기울임 ,  size : 폰트 크기
plt.title('하이닉스 candle chart', size=20)       ## 그래프 제목 입력
plt.xlabel("date(y-m-d)", size=15)        ## x축 라벨 입력
plt.ylabel("price(won)", size=15)         ## y축 라벨 입력


ax = fig.add_subplot(1,1,1)


count_skhynix = range(len(skhynix.index))                                 ## x축 스케일(눈금 개수/위치) 대입 값
# 예시 ) count_skhynix = range(1,5)   -> 아래 FixedLocator에 적용시 결과값 : 그래프에 2,3,4,5번째 눈금만 표시됨
ax.xaxis.set_major_locator(ticker.FixedLocator(count_skhynix))            ## x축 스케일(눈금 개수/위치)를 지정해줌.  값이 아닌 range 또는 list가 들어가야함
ax.xaxis.set_major_formatter(ticker.FixedFormatter(list(skhynix.index)))   ## x축 스케일(눈금)에 skhynix.index를 대입

mpl_finance.candlestick2_ohlc(ax, skhynix['Open'], skhynix['High'], skhynix['Low'], skhynix['Close'], width=0.5, colorup='r', colordown='b')
# width는 봉의 몸통 너비, 시가, 고가, 저가, 종가 순서이다.

plt.show()







########## barh (막대 세로 그래프),   bar (막대 가로 그래프) 차트 ###########
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from matplotlib import style

#그래프에서 한글이 깨지는 것을 개선해줌 (아래 구문 없으면 한글 깨짐)
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

style.use('ggplot')          ## 그래프 스타일 변경

# data 준비
industry = ['통신업', '의료정밀', '운수창고업', '의약품', '음식료품', '전기가스업', '서비스업', '전기전자', '종이목재', '증권']
fluctuations = [1.83, 1.30, 1.30, 1.26, 1.06, 0.93, 0.77, 0.68, 0.65, 0.61]


## barh 그래프 ##
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1,1,1)

ypos = range(10)
rects = plt.barh(ypos, fluctuations, align='center', height=0.5)
# barh 함수 , 첫번째 인자: 각 bar가 그려질 위치, 두번째 인자 : 값 (리스트 형태),  align은 bar 차트에서 bar의 정렬 위치를 설정,  height는 수평 bar 차트의 높이를 설정
plt.yticks(ypos, industry)  # 첫번째 인자 : y축 스케일 눈굼(개수/위치) 지정 인자,   두번째 인자 : y축 스케일 눈굼(개수/위치)에 대입될 값

#   text ,  각 막대 그래프에 해당 텍스트(수치)를 같이 출력
for i, rect in enumerate(rects):
    ax.text(0.95 * rect.get_width(), rect.get_y() + rect.get_height() / 2.0, str(fluctuations[i]) + '%', ha='right', va='center')
#  text의 첫번쨰 인자 : 텍스트(수치)를 출력해줄  x축 위치 지정 (여기서는 rect라는 bar의 넓이에서 95%의 위치가 됨)
#  두번쨰 인자 : 텍스트(수치)를 출력해줄  y축 위치 지정 (여기서는 bar의 y축 위치를 rect.get_y를 통해 얻은 후 bar 높이의 절반을 더함으로써 y축 위치를 계산)
#  세번쨰 인자 : 표현해줄 텍스트 내용
#  ha : horizontalalignment(정렬 기준)  - 적용값 {'center', 'right', 'left'}
#  va : verticalalignment(정렬 기준) - 적용값 {'center', 'top', 'bottom', 'baseline', 'center_baseline'}

plt.xlabel('등락률')
plt.show()


## bar 그래프 ##
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111)

pos = range(10)
rects = plt.bar(pos, fluctuations, align='center', width=0.5)
plt.xticks(pos, industry)

for i, rect in enumerate(rects):
    ax.text(rect.get_x() + rect.get_width() / 2.0, 0.95 * rect.get_height(), str(fluctuations[i]) + '%', ha='center', va = 'center')

plt.ylabel('등락률')
plt.show()








#################### 파이 (pie) 차트 출력하기 ################

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from matplotlib import style

# 그래프에서 한글 꺠지지 않게 하기
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
style.use('ggplot')  # 스타일 지정

# data 준비
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
labels = ['삼성전자', 'SK하이닉스', 'LG전자', '네이버', '카카오']
ratio = [40, 20, 10, 10, 10]
explode = (0.0, 0.1, 0.9, 0.0, 0.0)

plt.pie(ratio, explode=explode, labels=labels, colors=colors, autopct='%0.2f%%', shadow=True, startangle=90)
# 첫번째 인자 : 적용할 데이터
# explode : 파이 차트 모양을 떨어뜨려놓을 인자 지정 (피자 조각 꺼내기), 숫자만큼 피자 조각을 떨어뜨려 놓음
# colors : 각 인자별 차트 색깔
# autopct : 각 범주가 데이터에서 차지하는 비율을 출력 (퍼센티지, %)   ,  0.2f는 소수둘째자리까지만 출력되도록 formatting한 것
# startangle  :   0이 시계기준으로 3시 위치 , 60이면 1시위치, 90이면 12시 위치  (회전 방향은 반시계방향)

plt.show()




#################### histogram(히스토그램) +  y축 출력 범위 지정 + for문 활용 ################


for i in range(5):
    if i != 0:
        x = activations[i - 1]
    w = np.random.randn(node_num, node_num)
    plt.subplot(1, hidden_layer_size, i + 1)
    plt.title(str(i + 1) + "-layer's input", rotation=20)
    if i != 0:
        plt.yticks([], [])
    plt.hist(np.dot(x, w).flatten(), bins=50, range=(-2, 2))
    plt.ylim([0, 5000]) ###  y축 출력 범위 지정,   x축은  plt.xlim
plt.show()






