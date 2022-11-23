# <상위, 하위 폴더 경로 및 절대 경로 설정>

# 폴더 현황 :
# - 6509504
#    -PycharmProjects
#       -untitled
#          -pkg
#              : t1.py (현재 파일)
#    -python_v_test
#       -pkg
#           : fibonacci.py (목표 파일)
#       -test_folder
#           -test_ok
#               : ok.py


## 상위 폴더 경로 및 절대 경로 설정    sys.path.append(), sys.path.insert(index, 절대경로)
# https://blog.naver.com/pk3152/221355973475
# https://codechacha.com/ko/how-to-import-python-files/
# https://brownbears.tistory.com/296
# https://data-newbie.tistory.com/495
# https://blog.naver.com/smilewhj/221079181059     ## 이건 os 클래스에 대한 내용


import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))  ## 2개 상위 폴더로 이동함
print(sys.path[-1])   ## 출력결과:  C:\Users\6509504      , path에 새로운 경로가 최신으로 추가됨 확인
print(sys.path[0])    ## 출력결과:  C:\Users\6509504\PycharmProjects\untitled\pkg     , 기존 경로 확인

# sys.path.append((os.path.dirname(os.path.abspath(os.path.dirname(__file__)))))  ## 1개 상위 폴더로 이동함
# print(sys.path[-1])   ## 출력결과: C:\Users\6509504\python_v_main\Scripts


sys.path.append(r'C:\Users\6509504\python_v_main\Scripts')          ## 절대경로를 직접 주소로 입력하는 방법
print(sys.path[-1])   ## 출력결과:  C:\Users\6509504      , path에 새로운 경로가 최신으로 추가됨 확인

print(len(sys.path))  ## 출력결과:  12
sys.path.insert(12, r'C:\Users\6509504\python_v_main\Scripts')   ## 맨 마지막 index에 절대경로를 추가함
print(sys.path[12])   ## 출력결과: C:\Users\6509504\python_v_main\Scripts


from pkg.fibonacci import Fibonacci
print(Fibonacci.fib1(5))    ## Fibonacci 활용 가능하게됨
print(os.getcwd())  ## 현재 작업경로 출력, C:\Users\6509504\python_v_main\Scripts


## 하위 폴더 경로 설정

# 폴더 현황 : 맨 위 참조


from test_folder.test_ok.ok import ok          ## test_ok 내 ok.py로부터(from) ok 클래스를 import함
a=ok().gos()    ## gos는 ok 내 함수



## __init__ 의 활용
# https://blog.naver.com/hankrah/222436377837

: 파이썬이 해당 디렉터리를 참조하여, 하위 모듈을 참고하도록 하는 파일
 (Python 3.3 이후부터는 init 파일이 없어도 패키지로 인식이 가능)



## 파일명과 확장자 분리

import os
filename, fileExtension = os.path.splitext('test.zip')
filename, fileExtension
# 출처: https://takeardor.tistory.com/16 [기록하고 싶은 기록들:티스토리]



# 변수명에 문자열 넣기  1. globals(), 2. locals()

user_input = 'ab1'
globals()[user_input] = 50
print(ab1)  # 출력 : 50
print(type(ab1))  # 출력 : <class 'int'>




###print문
#  sperator / end / format / %d %s %f / escape '\' / raw string
#  연산기호 / 멀티라인 출력 / 
 
#separator 사용
print('t','e','s','t')  #''로 구분하면 문자끼리 띄워써짐
print('t','e','s','t',sep=' ')#문자 사이에 공백을 넣는다
print('t','e','s','t',sep='-')#문자 사이에 -를 넣는다
print('t','e','s','t',sep='')#sep 사이에 공백없음을 붙임 -> 즉 공백없이 붙인다
print('t','e','s','t',sep="")# 똑같음
print('niceman', 'gmail.com', sep ='@')


#end 옵션 사용
print('welcome to', end=' ') #끝에 공백과 띄어쓰기를 없앰, 즉 다음 문장이 붙여짐
print('~korea', end='!!') #끝에 느낌표를 붙임



#format 옵션
print('{} and {}' .format('you', 'me'))
print('{} + {} = {}' .format(1,2, 1+2))
#format에 인덱스 붙이기
print('{0}와 {1}중에 난 {0}가 더 좋다' .format('사과', '딸기')) 
print('{a}와 {b}중에 난 {a}가 더 좋다' .format(a='사과', b='딸기')) 
# 변수 선언후 format 활용
name = '슬기'
print(f'내 사랑은 {name}뿐이다') # f와 {변수} 조합



# %s : 문자, #d: 정수, %f : 실수
print("%s의 가장 좋아하는 정수는 %d 이고 실수는 %f이다" %('상큼이', 7, 12.2)) 
print("%5d와 %0.3f를 출력하라" % (2.5, 35123.33178))#정수 / 실수 소수자리 버리기



#format 과 %d / %s / %f 혼합 사용
print("{0:2d} 와 {1: 0.3f} 숫자중에 난 {0: 2d} 가 좋다" .format(121233, 3.3377))
## 121233을 정수로 표현하되(d), 최소 2자리는 넘도록 (2d, 이 경우는 숫자가 이미 6자리이므로 6자리로 표현됨)
## 3.3377을 소수 3째짜리까지만 표기(0.3f)

print("{0: 10f} 와 {1: 0.7f} 숫자중에 난 {0: 2d} 가 좋다" .format(121233, 3.3377))
## 121233을 소수로 표현하되(f), 최소 10자리는 넘도록 (10f, 이 경우는 숫자가 6자리이므로 빈칸 4자리가 앞에 추가됨)
## 3.3377을 소수 5째짜리까지만 표기(0.5f, 이 경우는 소수 5번째자리가 0으로 표현됨 -> 3.3377000)

# escape 코드 
print ('  "내가 너한테 말했지!" ')  # 따옴표 출력하기
print(' test \n')   #\n 띄워쓰기 표현하기
print('\t\t\ttest') #\t는 tap 버튼을 의미함, tap 3번누른만큼 이동하여 출력



##연산 기호
x=-2
y=5
z=3
a = x//y    #//는 나눗셈의 몫
b= x%y     #%는 나눗셈의 나머지
print(abs(x))  #절대값
print(x*y)
print(x**y)  # x의 y제곱
print(pow(x,z))   # x의 y제곱
n, m =divmod(x,y)  #x에서  y를 나눈 몫을 n으로, 나머지는 m으로



# 이스케이프 문자(\) 사용,   \를 통해 뒤에 있는 문자가 그냥 문자라는 것을 알려줌      
# \를 이용해 문자열 내 따옴표(") 사용
escape_str1 = "Do you have a \"big collection\"?"  
escape_str2 = 'What\'s on TV?'
escape_str3 = "What's on TV?"
escape_str4 = 'This is a "book".'
print(escape_str1)
print(escape_str2)
print(escape_str3)
print(escape_str4)

# Raw String    
# \가 이스케이프 문자가 아니라 그냥 문자라는 것을 알려줌,
#  주로 파일 경로때 많이 쓰임
raw_s1 = r'C:\Programs\python3\"'
raw_s2 = r"\\a\b\c\d"
raw_s3 = r'\'"'
raw_s4 = r"\"'"
print(raw_s1)
print(raw_s2)
print(raw_s3)
print(raw_s4)



# 멀티라인 출력,    \를 통해 다음줄에 나오는 것들도 이어지게 할수 있음
multi_str1 =  """후 \
    문자열
    멀티라인
    테스트
    """
print(multi_str1)

multi_str2 = \
    """
    문자열
    멀티라인
    테스트
    """
print(multi_str2)

multi_str3 = \
    '''
    문자열 멀티라인 
    역슬래시(\) \   
    테스트
    '''                #중간에 역슬러쉬가 들어가면 멀티라인 해제됨
print(multi_str3)
  

###문자열   
# in / dir / capitalize / endwith /join / replace / split / sorted
#  reversed / islower / len() / 인덱싱과 슬라이싱 / lower()와 upper()

# 문자열 연산 'in'
str_o1 = "Niceman"
str_o2 = "Orange"
str_o3 = "this is string example....wow!!! this is really string"
str_o4 = "Kim Lee Park Joo"

print(3 * str_o1)
print(str_o1 + str_o2)
print(dir(str_o1))         # dir은 함수나 변수의 내부 속성을 알려주는 함수
print('x' in str_o1)       #str_01에 x가 있니? 있으면 true, 없으면 false 반환
print('i' in str_o1)
print('e' not in str_o2)   #str_01에 x가 없니? 없으면 true, 있으면 false 반환
print('O' not in str_o2)



# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp
str_o1 = "niceman"
str_o2 = "Orange"
str_o3 = "this is string example....wow!!! this is really string"
str_o4 = "Kim Lee Park Joo"
print("Capitalize: ", str_o1.capitalize())   #앞글자만 대문자화
print("endswith?: ", str_o2.endswith("s"))   #끝에 ()안의 글자로 끝나는지? TRUE/FALSE 반환
print("join str: ", str_o1.join(["I'm ", "!"])) # 앞뒤로 글자를 붙임, 더 정확히는 LIST 원소 사이사이에 STR_01이 삽입됨
print("replace1: ", str_o1.replace('Nice', 'Good')) #글자를 대체함
print("replace2: ", str_o3.replace("is", "was", 3)) #글자를 3번만 대체함
'ababab'.replace('ab','*', 1) ## 출력 '*abab'  , replace 를 1번만 실행  # https://ooyoung.tistory.com/77
#  '변수. replace(old, new, [count])' 형식에서
# - old : 현재 문자열에서 변경하고 싶은 문자
# - new: 새로 바꿀 문자
# - count: 변경할 횟수. 횟수는 입력하지 않으면 old의 문자열 전체를 변경한다. 기본값은 전체를 의미하는 count=-1로 지정되어있다.

print("split: ", str_o4.split(' '))  # Type 확인    #""사이의 글자로 구분지음, LIST로 반환
print("sorted: ", sorted(str_o1))  # reverse=True, 문자열을 글자 오름차순으로 정렬, LIST로 반환
print("reversed2: ", list(reversed(str_o2))) #문자열을 글자 하나하나 거꾸로 list와 같이 사용
print("reversed1: ", reversed(str_o2))  #LIST 안쓰면 작동안됨
print("a".islower()) # a라는 문자가 소문자입니까? TURE/FALSE 반환 
print(str_01[0:3])   # str_01 문자열

a="NiceMan"
print(a.lower(), a.upper())  #소문자 변환, 대문자 변환


# 문자열 슬라이싱(인덱싱)
# 일부분 추출(정말 중요)
str_sl = 'Niceboy goodman'
print(str_sl[0:3])   #index 0부터 2번쨰 원소까지 출력(뒤 숫자의 index는 출력하지 않음)
print(str_sl[:len(str_sl)])  #index 0부터 문자길이 index n-1개만큼 출력, 즉 문자 전체 출력 
print(str_sl[:len(str_sl) - 1]) #index 0부터 문자길이 index n-2개만큼 출력, 즉 문자 -1만큼 출력 
print(str_sl[:])    #문자 전체 출력
print(str_sl[1:7:2])  #index 1부터 6까지 출력, 2개씩 건너뛰면서
print(str_sl[-3:15])  # -3 index부터(문자끝이 -1, 그 옆이 -2,-3순) 14번 index까지 출력  
print(str_sl[1:-2])   # index 1부터 -2까지
print(str_sl[::-1])   # 문자열 전체를 출력하나 -1만큼씩, 즉 문자열을 거꾸로 출력  
print(str_sl[::2])    # 문자열 전체를 출력하나 2만큼씩

#index 함수를 이용한 문자열 추출
a= "niceman"
print(a[4:])
man_index = a.index("man")
print(a[man_index: man_index+3])



### 형 변환,          list 형변환, tuple 형변환

#for 문을 이용한 list 형 변환 출력
tup = (1, 2, 3, 4)   
print([s for s in tup])



### deque(데크)

### 자료형(순서O, 중복O, 수정O, 삭제O)    - List와 같음

# Deque(데크)는 double-ended-queue의 줄임말
# 스택과 큐의 기능을 모두 가짐
# 출입구가 양쪽에 있음
# 리스트보다 월등히 속도 빠름
# https://wellsw.tistory.com/122    :  빠른 이유(시간 복잡도)

# 스택과 큐는 둘다 데이터를 차곡차곡 쌓아올린 형태의 자료구조이다.
# 스택(Stack)은 나중에 넣은 데이터가 먼저 나오는 형태, (후입선출)
# 큐(Queue)는 먼저 넣은 데이터가 먼저 나오는 형태이다. (선입선출)
# 참고로 덱(Deque)은 스택과 큐를 합친 형태이다
# 출처: https://mygumi.tistory.com/357 [마이구미의 HelloWorld]


from collections import deque        ## import 선언 필요

deq = deque()    ## 데크 생성

## append / appendleft
deq.append(1) # Add element to the end
deq.appendleft(0) # Add element to the start
deq.append(10) # Add element to the end

print(deq)  # 출력 : deque([0, 1, 10])


## pop / popleft
deq.popleft()  # Pop element from the start
deq.pop()  # Pop element from the end

print(deq)   # 출력 : deque([1])


## extend / extendleft
deq.extend([1,2,3,4,5])  ## 우측(마지막)에 추가
deq.extendleft([1,2,3,4,5])   ## 좌측(처음)에 추가

print(deq)  # 출력 : deque([5, 4, 3, 2, 1, 1, 1, 2, 3, 4, 5])


## rotate(n)  : n만큼 회전시킴
deq.rotate(1)     # 1만큼 회전시킴 (우측으로 1칸씩 이동)
print(deq)    # 출력 :  deque([5, 5, 4, 3, 2, 1, 1, 1, 2, 3, 4])

## 문자열 적용
deq2 = deque('love')
print(deq)    # 출력 :  deque(['k', 'l', 'o', 'v', 'e'])


## insert
deq2.insert(0,'k')   ## 인덱스와 원소 같이 지정해줘야됨
print(deq)    # 출력 :  deque(['k', 'l', 'o', 'v', 'e'])


## remove
deq2.remove('k')   # 원소로 제거 (인덱스 아님, pop은 무조건 최우측 / popleft 무조건 최좌측)
print(deq)    # 출력 :  deque(['l', 'o', 'v', 'e'])


## reverse   (뒤집기)
deq2.reverse()
print(deq)    # 출력 :  deque(['e', 'v', 'o', 'l'])




### 리스트(list), 튜플

### 리스트 자료형(순서O, 중복O, 수정O, 삭제O)
#인덱싱과 슬라이싱 / 연산
# append / extend / sort / reverse /insert /remove / pop /del /index /count

# 선언
a = []
b = list()
c = [1, 2, 3, 4]
d = [10, 100, 'Pen', 'Cap', 'Plate']
e = [10, 100, ['Pen', 'Cap', 'Plate']]

# 리스트 컴프리헨션(list comprehension) 선언
z= list(range(1,100))
z= [x for x in range(1,101)]

# 인덱싱
print('#=====#')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
#print('e - ', e[-1][1][4])   #실행시켜보면, list의 범위를 넘어선 index를 지정하면 실행안됨
print('e - ', list(e[-1][1]))

# 슬라이싱
print('#=====#')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])    #2차원 배열에서도 슬라이싱 가능함

# 리스트 연산
print('#=====#')
print('c + d - ', c + d)  #단순히 리스트가 합쳐짐 (인덱스는 덧셈 순서에 영향을 받음)
print('c * 3 - ', c * 3)  #리스트가 3개 합쳐짐 c+c+c와 같은 효과
# print("c[0] + 'hi' - ",c[0] + 'hi')
print("'hi' + c[0] - ", 'hi' + str(c[0]))

# 리스트 수정, 삭제
print('#=====#')
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c']  #list에서 index 1 위치에 리스트의 원소로 대체됨 (1차원 리스트 유지)
print('c - ', c)
c[1:3] = ['a', 'b', 'c']  #list에서 index 1,2 위치에 리스트의 원소로 대체됨 (1차원 리스트 유지)
print('c - ', c)
c[1] = ['a', 'b', 'c']   #list에서 index 1 위치에 리스트 자체가 들어감 (2차원 리스트 변환)
print('c - ', c)
c[1:3] = []
print('c - ', c)

print(c.remove(1))  # 1이라는 원소값을 삭제 (괄호안 index 아님)
del c[3]            #index 3 원소 삭제  (괄호안 index)
print('c - ', c)



# 리스트 함수 
# append / extend / sort / reverse /insert /remove / pop /del /index /count
# enurmerate
# join

a = [5, 2, 3, 1, 4]

a.append(6)           #원소 6을 추가함
print('a - ', a)
a.append([5, 2, 3, 1, 4])           #리스트 자체를 원소로써 추가함 (2차원 리스트 전환)
print(a)
print('a - ', a)
a.sort()  ## 사라진 기능
sorted(a) ## 이건 가능
print('a - ', a)
a.reverse()
print('a - ', a)
print('a - ', a.index(5))
a.insert(2, 7)      #2번 index에 숫자 7을 삽입함
print('a - ', a)
a.reverse()

a.remove(1)   # remove은 괄호안에 원소 값 자체를 받음, 괄호안에 엉뚱한 지정 값이 들어가면 삭제안됨
print('a - ', a)
a.pop()       # pop은 괄호안에 index 값을 받음, 괄호안 지정 index 없을시에는 맨뒤 삭제
print('a - ', a)

print('a - ', a.pop())
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))    #4라는 원소의 개수를 카운트함
ex = [8, 9]
a.extend(ex)              #리스트를 원소로써 일일이 추가함
print('a - ', a)

a = [5, 2, 3, 1, 4]
print(a.index(1))  #1이라는 원소를 가진 index를 반환함

# enumerate()        인덱스와 원소값 2개를 같이 반환
a= [1, 2, 3]
print(a.index(1))        #index함수로 직접 반환하는 방법
for i,v in enumerate(a): #enumerate 이용
    print(i,v)
for i in enumerate(a): #enumerate 이용 
    print(type(i), i)  # 변수를 1개만 받는 경우, tuple로 출력

# join    : list to string  (리스트를 문자로 변환)
print(''.join(list(reversed(name))))    ## 공백없이 문자끼리 합침
print('-'.join(list(reversed(name))))   ## 문자 사이의 -를 삽입한후 합침


# list count 기능

a = [1,2,3,13,1,1,1]
a.count(1)


### 튜플(tuple)     (순서O, 중복O, 수정X,삭제X)

ab = (1,)  #tuple 정의
cd= (1,2,3)
print(type(ab)) 
ef=(1)     #int 타입으로 정의됨
print(type(ef)) 


# index() / enumerate()        인덱스와 원소값 2개를 같이 반환
a= (1, 2, 3)
print(a.index(1))        #index함수로 직접 반환하는 방법
for i,v in enumerate(a): #enumerate 이용
    print(i,v)


### 딕셔너리, 집합 자료형

### 딕셔너리(dictionary) 자료형(순서X, 중복X, 수정O, 삭제O)
# 선언 / keys, values, items / in

# 선언
a = {'name': 'Kim', 'phone': '01012345678', 'birth': '870124'}
b = {0: 'Hello python!'}
c = {'arr': [1, 2, 3, 4]}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)

# 출력
print('a - ', a['name'])     # 이런경우 존재하지않는 key 값 호출시 -> 에러 발생
print('a - ', a.get('name')) # 존재하지않는 key 값 호출하여도 -> None 처리, 우수함
print('b - ', b[0])
print('b - ', b.get(0))
print('c - ', c['arr'])
print('c - ', c['arr'][3])    #arr에 대한 key값중 3번 index 호출
print('c - ', c.get('arr'))

# 딕셔너리 추가
a['address'] = 'seoul'     #key/value 한쌍 추가됨
print('a - ', a)
a['rank'] = [1, 2, 3]
print('a - ', a)

# 딕셔너리의 keys, values, items : 반복문(iterate) 사용 가능
print('a - ', a.keys())   
print('b - ', b.keys())   
print('c - ', c.keys())   
#위 출력시 결과값은 ['name': 'Kim', 'phone': '01012345678', 'birth': '870124']
# 리스트처럼 보여지나, 실제로 인덱싱해보면 인덱싱을 지원하지 않는다고 함

print('a - ', list(a.keys())) #인덱싱 사용을 위해서 list로 형 변환
print('b - ', list(b.keys()))
print('c - ', list(c.keys()))
temp = list(c.keys())
print(temp[1:3])              #인덱싱 사용

print('a - ', a.values())     #위와 마찬가지
print('b - ', b.values())
print('c - ', c.values())

print('a - ', list(a.values())) #인덱싱 사용을 위해서 list로 형 변환
print('b - ', list(b.values()))
print('c - ', list(c.values()))

print('a - ', a.items())      #items : key와 value 묶음
print('b - ', b.items())
print('c - ', c.items())

print('a - ', list(a.items()))
print('b - ', list(b.items()))
print('c - ', list(c.items()))
# [('name', 'Kim'), ('phone', '01012345678'), ('birth', '870124'), ('address', 'seoul'), ('rank', [1, 2, 3])]
# 위 출력시, 위와 같이 list안에 tuple로써 (key, value) 묶음으로 구성됨

# in 함수로 key 값 찾기
print('a - ', 'name' in a)
print('a - ', 'addr' in a)
print('a - ', 'kim' in a)  # value 값은 못찾음 








































### 집합(Set) 
# 자료형(순서X, 중복X)         ##순서가 없기떄문에, 인덱싱도 안됨
# 선언 / intersection() union() difference() add() remove()

# 선언
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)

##순서가 없기떄문에, 인덱싱도 안됨 -> 인덱싱을 위해서는 list / tuple로 변환필요
# 튜플 변환
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])
# 리스트 변환
l = list(c)
print('l - ', type(l), l)
print('l - ', l[0], l[1:3])

#set 함수    intersection() union() difference() add() remove()

#교집합 원소 구하기 '&' 또는 intersection()
print('l - ', s1 & s2)              # 교집합 원소 구하기
print('l - ', s1.intersection(s2))  # 교집합 원소 구하기 -> {4,5,6}

#합집합 원소 구하기 '|' 또는 union()
print('l - ', s1 | s2)             # 합집합 원소 구하기
print('l - ', s1.union(s2))        # 합집합 원소 구하기

#차집합 원소 구하기 '-' 또는 difference()
print('l - ', s1 - s2)             #차집합 원소 구하기, 순서 중요
print('l - ', s1.difference(s2))

# 원소 추가 (add) & 제거 (remove)
s1 = set([1, 2, 3, 4])
s1.add(5)   #원소추가, add      -   append 아님
print('s1 - ', s1)
s1.remove(2)  #원소제거, remove() 괄호 안이 원소값을 의미함, index 아님
print('s1 - ', s1)








### 조건문 if 실습



# 예1
if True:
    print("Yes")  # 들여쓰기 중요

if False:
    # 출력되지 않음.
    print("No")


# 관계연산자   >, >=, <, <=, ==, !=
# 논리연산자   and, or, not
### 산술 > 관계 > 논리 순서로 우선 순위 적용

### 참 거짓 종류
# 참 : "내용", [내용], (내용), {내용}, 1, true   -> if "사랑해"  = true로 적용
# 거짓 : "", [], (), {}, 0, None, false         -> if ""       = false로 적용

a = 100 , b = 60 , c = 15
print('not : ', not a > b)
print('ex1 : ', 3 + 12 > 7 + 3)
print('ex2 : ', 5 + 10 * 3 > 7 + 3 * 20)
print('ex3 : ', 5 + 10 > 3 and 7 + 3 == 10)      # 산술 > 관계 > 논리 순서
print('ex4 : ', 5 + 10 > 0 and not 7 + 3 == 10)  # 산술 > 관계 > 논리 순서


## if문 사용  if, elif, else
score1 = 90
score2 = 'A'

# 복수의 조건이 모두 참일 경우에 실행.
if score1 >= 90 and score2 == 'A':
    print("합격하셨습니다.")
else:
    print("불합격입니다.")

id1 = "gold"
id2 = "admin"
grade = 'super'

if id1 == "gold" or id2 == "admin":
    print("관리자 로그인 성공")

if id2 == "admin" and grade == "super":
    print("최고 관리자 로그인 성공")

is_work = False

if not is_work:
    print("is work!")

# 다중 조건문
num = 90

if num >= 70:
    print("num ? ", num)
elif num >= 60:
    print("num ? ", num)
else:
    print("default num")

# 중첩 조건문

age = 27
height = 175

if age >= 20:
    if height >= 170:
        print("A지망 지원 가능")
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원 불가")
else:
    print("20세 이상 지원가능")

# in, not in

q = [1, 2, 3]
w = {7, 8, 9, 9}
e = {"name": 'Kim', "city": "seoul", "grade": "B"}
r = (10, 12, 14)

print(1 in q)
print(6 in w)
print(12 not in r)
print("name" in e)  # key 검색
print("seoul" in e.values())  # value 검색





### 기본 반복문 사용(while, for)
v1 = 1

while v1 < 11:               # v=10일때까지 반복함 즉 1~10 열 번 반복
    print("v1 is :", v1)
    v1 += 1

## for문은 range 또는 list와 궁합이 좋다
## break / continue / flag 함수 / for-else(+break) 사용

for v2 in range(11):         # 마지막 수 미실행, v=1~10일때까지 반복함 
    print("v2 is :", v2)

for v4 in range(1, 11, 2):   # 마지막 수 미실행, v=1~10일때까지 2계단씩 반복함
    print("v4 is :", v4)


# 시퀀스(순서가 있는) 자료형 반복
# 문자열,리스트,튜플,집합,사전   -집합(set)과 사전(dict)은 순서 없지만 사용가능?
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip


#리스트 반복
names = ["Kim", "Park", "Cho", "Lee", "Choi", "Yoo"]
for name in names:               
    print("You are", name)


#문자열 반복
word = 'dreams'
for s in word:             
    print('word : ', s)

#dictionary 반복
my_info = {"name": "Kim","age": 33,"city": "Seoul"}

for i_key in my_info:              #key값을 이용한 key 반복, 
    print(i_key)                   # 기본값은 key로 출력됨
print("=====")

for i_key in my_info.keys():       #key값을 이용한 key 반복
    print(i_key)
print("=====")

for i_value in my_info.values():    #key값을 이용한 value 반복
    print(i_value)
print("=====")

for i_key in my_info:               #key값을 이용한 value 반복
    print(my_info[i_key])           #dict[key] = my_info["city"]
print("=====")

for key,value in my_info.items(): #key / value를 이용한 item 전체 반복
    print(key,":", value)

for item in my_info.items(): # item을 하나의 변수로 받기 (tuple로 받음)
    print(item)



# break / continue / flag 

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

# break          -for문 탈출
for num in numbers:
    if num == 33:
        print("found : 33!")
        break                      #for문 종료
    else:
        print("not found : ", num)

# for-else (+break)       -for문이 정상 종료시 else문 진입
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:  # 45
        print("found : 33!")
        break
    else:
        print("not found : ", num)

else:    ##for문이 정상 종료시 else문 진입함. 그러나 break로 나가질경우 미진입
    print("Not Found 33!") # numbers에 33 없다면 break 미실행됨 -> else 실행

# continue             -그 아래 단계를 실행하지않고, 다음 차례로 반복실행함
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:  #type이 실수일때만, type을 미출력하고 다음 단계실행
        continue 

    print("type:", type(v))
    print("multiply by 2:", v * 3)

# flag 사용

f = True
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

while f:
    for v in numbers:
        if v == 33:               #33을 찾았으므로
            print("found : 33!")
            f = False             #f=false 되어, for문 종료시 while문 반복종료 
        print("not found : ", v)


# 자료 구조 변환 예제
name = 'Niceman'
print('reversed : ', reversed(name))
print('list : ', list(reversed(name)))
print('list : ', tuple(reversed(name)))
print('list : ', set(reversed(name)))  # 순서X

# Join    : list to string  (리스트를 문자로 변환)
print(''.join(list(reversed(name))))    ## 공백없이 문자끼리 합침
print('-'.join(list(reversed(name))))   ## 문자사이의 -를 삽입한후 합침


#리스트 컴프리헨션(list comprehension) 이용한 for문
q4 = ["nice", "study", "python", "anaconda", "!"]
for i in q4:
    if len(i) >=5:
        print(i)

print( [x for x in q4 if len(x)>=5])   ##위 for문이 1줄로 가능해짐


q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
q7 =[]
for i in q6:
    if i.islower():
        q7.append(i.upper())
    elif i.isupper():
        q7.append(i.lower())
    else:
        print("이상 조건에 빠짐")
print(q7)

##위 for문이 아래 1줄로 가능해짐  (elif는 사용불가)
print([ x.upper() if x.islower()  else x.lower() for x in q6])



# defaultdict(기본값 있는 dictionary) - collections 모듈
# https://appia.tistory.com/218

import collections

normalDict = collections.defaultdict(int)
# 또는
normalDict = collections.defaultdict(float)

normalKey = ["A", "B", "C"]

for item in normalKey:
    normalDict[item]

print(normalDict)        # 출력 : defaultdict(<class 'int'>, {'A': 0, 'B': 0, 'C': 0})
print(normalDict['A'])   # 출력 : 0.0





### 파이썬 함수 및 람다(lambda)

### 함수 
# 다중리턴 / 중첩리턴 / *arg / **kwargs / 입력값 복합(일반 + *arg + **kwargs)
# 튜플 리턴 / 리스트 리턴 / 딕셔너리 리턴 / hint 주기

#함수 값 입력과 리턴값
def hello_return(world):   ##input 값 : world
    value = "Hello, " + str(world)
    return value           ##return 값: value

str = hello_return("Niceman")      
print(str)


#다중리턴(return)

def func_mul1(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return y1, y2, y3          ##리턴값 3개 !!!

val1, val2, val3 = func_mul1(3)   ## 리턴값 개수에 맞게 변수 정의
print(val1, val2, val3)


# 튜플 리턴
def func_mul2(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return (y1, y2, y3)     ### 리턴값을 튜플로 지정함 (y1, y2, y3) 

tup = func_mul2(4)
print(type(tup), tup, list(tup))


# 리스트 리턴
def func_mul2(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return [y1, y2, y3]     ### 리턴값을 튜플로 지정함 [y1, y2, y3]


lis = func_mul2(6)

print(type(lis), lis, set(lis))


# 딕셔너리 리턴
def func_mul3(x):
    y1 = x * 2
    y2 = x * 4
    y3 = x * 6
    return {'ret1': y1, 'ret2': y2, 'ret3': y3}  
    ### 리턴값을 딕셔너리로 {'ret1': y1, 'ret2': y2, 'ret3': y3} 


dic = func_mul3(8)

print(type(dic), dic, dic.get('ret3'), dic.items(), dic.keys(), dic.values())


## *args(아규),  **kwargs(키워드? 키워그?) 이해

# *args  (*를 변수명 앞에 넣어줌)
def args_func(*ar):    # 매개변수를 크기/개수 자유롭게 튜플(tuple) 형태로 넘겨줌
    print(ar, type(ar)) 

args_func('Kim')
args_func('Kim', 'Park')       #튜플로 함수에 인풋 입력
args_func('Kim', 'Park', 'Lee')


def args_func(*args):  # 매개변수를 크기/개수 자유롭게 튜플(tuple) 형태로 넘겨줌 
    for i, v in enumerate(args):
        print('{}'.format(i), v, end =' ')
args_func('Kim')
args_func('Kim', 'Park')
args_func('Kim', 'Park', 'Lee')

print()


# **kwargs (**를 변수명 앞에 넣어줌)

def kwargs_func(**kwargs): #매개변수를 크기/개수 자유롭게 딕셔너리 형태로 넘겨줌 
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v], end=' '+'\n')

kwargs_func(name1='Kim')   
kwargs_func(name1='Kim', name2='Park') #딕셔너리로 함수에 인풋 입력
kwargs_func(name1='Kim', name2='Park', name3='Lee')

# 출력 :
# name1 Kim
# name1 Kim
# name2 Park
# name1 Kim
# name2 Park
# name3 Lee


# 입력값 전체 혼합  (일반 인풋 + *arg + **kwargs)
def example(arg_1, arg_2, *args, **kwargs):
    print(arg_1, arg_2, args, kwargs)

example(10, 20)     # 함수 실행 가능, *arg와 **kwargs는 필수 입력값이 아님
                    # 즉, 유연한 함수 입력이 가능해진다
example(10, 20, 'park', 'kim', 'lee')
example(10, 20, 'park', 'kim', 'lee', age1=33, age2=34, age3=44)
# 입력값 2개 이후로는 튜플(arg)로 판단하며, 
# 딕셔너리(kwargs) 형태가 나타날떄까지 튜플로 취급함


# 중첩함수
def nested_func(num):
    def func_in_func(num):
        print(num)

    print("In func")
    func_in_func(num + 100)
nested_func(1)



# 함수에 Hint(힌트) 주기

def tot_length1(word: str, num: int) -> int:  
#word: str, num: int  word 입력값이 str형, num 입력값이 int형이라고 힌트를 줌 
# -> int        의 뜻은 반환값 즉 리턴값 type이 int라는 의미
# 그러나, hint의 타입과 다르게 값이 입력되거나, 반환되어도 문제없음

    return len(word) * num
print('hint exam1 : ', tot_length1("i love you", 10))

def tot_length2(word: str, num: int) -> None:  #입력type str&int, 리턴값 없음
    print('hint exam2 : ', len(word) * num)
tot_length2("niceman", 10)




### 람다 (lambda)
# 메모리 절약, 가독성 향상, 코드 간결
# 코드 상에서 한번만 사용되는 기능이 있을 때, 굳이 함수로 만들지 않고 
# 1회성으로 만들어서 쓸 때 사용
## 함수는 객체 생성 -> 리소스(메모리) 할당   
## 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화


## 일반적 함수     -> 변수로서 메모리에 미리 할당됨
def mul_10(num):
    return num * 10
mul_func = mul_10 
#mul_10함수가 객체로서 mul_func의 대입값이 되었음 즉, mul_func도 함수가 됨 
print(mul_func(5))   
print(print(type(mul_10)))         #확인시 type: function 출력됨. 객체라는 뜻
print(print(type(mul_func)))       #확인시 type: function 출력됨. 객체라는 뜻


## 람다 함수 -> 할당
lambda_mul_func = lambda num: num * 10   
#num값을 입력받아, num*10으로 반환하는 람다함수


##일반적 함수 ex1)
def func_final(x, y, func):
    print(x * y * func(10))
def mul_func(x):
    return x*10
func_final(10, 10, mul_func)

##람다 함수 ex1)
func_final(10, 10, lambda x : x*10 )

## 람다 for문
a = [x for x in range(0,5)]  ## [0, 1, 2, 3, 4]

### map 함수   : list와 같이 사용
list(map(mul_func, [x for x in range(0,5)]))  ## [0, 10, 20, 30, 40]





###  클래스 (class)
# Self, 클래스, 인스턴스(instance) 변수

# 네임스페이스 : 변수 저장 공간

# 변수의 종류 2가지 - 클래스, 인스턴스 
 # 클래스 변수 : class에서 직접 선언되는 변수, 객체보다 먼저 생성
 # 인스턴스 변수 : 객체(인스턴스)마다 별도로 존재, 인스턴스 생성 후 사용


### 클래스(class)  (속성 / 메소드로 이루어짐)


class User_info:  #클래스 네이밍의 첫글자는 대문자로 해야함
     #__inti__(생성자) 메소드 
    def __init__(self, name, height, age): 
        #self는 인스턴스를 갖는다는 것을 의미함, name/height/age는 인스턴스의 속성들이 됨       
        self.name = name   
        self.height = height
        self.age = age
    def print_info(self):           #print_info 메소드
        print("Name: " + self.name)

    def __del__(self):             # 소멸자 메소드 (인스턴스를 삭제할때 쓰임)
        print("Instance removed!")


a1=User_info('lee', 180, 33)    #a1 인스턴스 생성
a2=User_info('kim', 175, 34)    #a2 인스턴스 생성
a1.print_info()
a2.print_info()

print(id(User_info))       # id: user_info 클래스의 네임스페이스(저장공간) 
print(id(a1))              # id: a1이라는 인스턴스의 네임스페이스(저장공간)
print(a1.__dict__)         #딕셔너리 형태로 변수이름과 해당 값을 출력


### self의 이해  
### self란 메소드 함수에서 객체화된 인스턴스 자기자신(아래 예시에서 a1_test)을 의미함

class SelfTest:
    def function1():   ### 'self'라는 클래스 인스턴스가 없으므로, 클래스 함수가됨
        print("function1 called!")

    def function2(self): ###'self'가 있으므로 메소드 함수가 되며, 펑션2 함수는 self 즉 인스턴스를 입력받음
        print(id(self))  ### 각 인스턴스의 네임 스페이스 id가 출력됨  
        print("function2 called!")

a1_test = SelfTest()
#a1_test.function1() # function1은 클래스 함수이므로 
                     # 인스턴스 함수 호출방식으로 실행안됨
SelfTest.function1() #function1을 호출하고 싶다면, 이렇게 클래스로 호출해야함
a1_test.function2()  #function2는 메소드 함수이므로, 인스턴스로 호출 가능함

#SelfTest.function2() # <-function2는 메소드 함수라 클래스 방식으로
                      #  호출하면 실행안됨
SelfTest.function2(a1_test) #이렇게 self 인자 또는 인스턴스(a1_test)를 입력값으로
                            #넣어주면 클래스 방식으로도 실행가능
                        
### 즉, self란 메소드 함수에서 객체화된 인스턴스 자기자신(a1_test)을 의미함




# print(SelfTest.function2()) #예외 발생


# 클래스 변수 , 인스턴스 변수
class Warehouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        # 인스턴스 변수
        self.n = name
        Warehouse.stock_num += 1

    def __del__(self):         ## 인스턴스를 삭제할때 쓰는 함수
        Warehouse.stock_num -= 1


user1 = Warehouse('Kim')
user2 = Warehouse('Park')
user3 = Warehouse('lee')
print(user1.n)
print(user2.n)
print(user3.n)
print(user1.__dict__)   # {'n': 'Kim'} 출력
print(user2.__dict__)   # {'n': 'Park'} 출력
print(user3.__dict__)   # {'n': 'lee'} 출력
print(Warehouse.__dict__)    # 클래스 네임스페이스 , 클래스 변수 (공유)  ->  'stock_num': 3 출력

# Warehouse.stock_num = 50   # <-이렇게 직접으로 접근도 가능

print(user1.stock_num)            #user 1/2 똑같이 3출력 
print(user2.stock_num)            #인스턴스 사이에서도 클래스 변수는 공유됨
#클래스 변수인 stock_num을 인스턴스에서 직접 호출가능 
#자기 네임스페이스에 해당 변수가 없으면, 클래스가서 찾음 (여기서도 없으면 에러)

del user3                   # user3 인스턴스 삭제
print(user1.stock_num)      # user3 인스턴스 삭제하면서, 클래스 변수 stock_num도
print(user2.stock_num)      # -1 되었기때문에 user 1/2도 2로 출력됨 

## 클래스 연습
class Learn_member:
    members =0

    def __init__(self, name, study, attitude):
        Learn_member.members +=1
        self.name = name
        self.std = study
        self.att = attitude

    def __del__(self):
        Learn_member.members -=1


    def show (self):
        print(self.name, self.std, self.att)

    def show2():
        print("러닝랩 멤버의 수는", Learn_member.members)

aa1 = Learn_member('lee', "hard", "good")
aa2 = Learn_member('kim', "hard", "good")
aa3 = Learn_member('park', "normal", "soso")
aa1.show()
Learn_member.show2()
del aa3
Learn_member.show2()
print(dir(Learn_member))
print(id(Learn_member))





### 파이썬 클래스 상속, 다중상속

### 상속 
# 슈퍼클래스(부모) 및 서브클래스(자식) 
# 서브클래스는 슈퍼클래스의 모든 속성, 메소드 사용 가능 (상속받음)
# 오버라이딩(# Method Overriding), parent method call, 상속관계 출력 [.mro()] 

"""Parent Class (슈퍼클래스 / 부모클래스)"""
class Car:
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
         print('Car Class "Show" Method!')
        #return 'Car Class "Show" Method!'


"""Sub Class (서브클래스 / 자식클래스)"""
class BmwCar(Car):              # (car)를 통해 car class 상속
                                # 상속을 통해 car class의 속성/메소드 사용가능
    def __init__(self, car_name, tp, color): #tp, color는 슈퍼클래스 속성이므로
        super().__init__(tp, color)  #슈퍼클래스의 속성/메소드임을 명시함   
        self.car_name = car_name     #car_name은 서브클래스 속성         

    def show_model(self) -> None:    # hint 사용, return 값 없다
        return 'Your Car Name : %s' % self.car_name

"""Sub Class (서브클래스 / 자식클래스)"""
class BenzCar(Car):        # (car)를 통해 car class 상속

    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)  #super 클래스의 tp, color를 sub에서 정의
        self.car_name = car_name     #sub 클래스의 name을 sub에서 정의 

    def show(self):
        super().show()         #super 클래스의 show 메소드 함수를 sub에서 활용 
        return 'Car Info : %s %s %s' % (self.car_name, self.color,self.type)

    def show_model(self) -> None:
        return 'Your Car Name : %s' % self.car_name


# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color)  # Super class에서 불러온값
print(model1.type)  # Super class에서 불러온값
print(model1.car_name)  # Sub class에서 불러온값
print(model1.show())  # Super class에서 show 메소드 불러옴
print(model1.show_model())  # Sub class에서 불러온값
print(model1.__dict__)  #model1 딕셔너리 형태로 변수명과 값 불러오기

# Method Overriding   
 #슈퍼클래스에서 정의된 메소드 함수를 서브클래스에서 불러 쓰는 것
 #이때, sub에서 코딩을 추가함으로써 기능 추가 가능함 (위 예, 'car info:' 출력 추가)
model2 = BenzCar("220d", 'suv', 'black')
print(model2.show())  #실행시, 슈퍼클래스와 서브클래스의 메소드 모두 실행됨

# Parent Method Call
 #슈퍼클래스의 메소드를 호출하는것, benzcar에서 show 메소드의 경우, 
 # 위 예에서 super.show()를 통해 슈퍼클래스의 메소드도 호출하게 설계되어짐
model3 = BenzCar("350s", 'sedan', 'silver')
print(model3.show())

# Inheritance Info   ".mro()"
 # 상속관계 / 상속정보를 보여줌 
print('Inheritance Info : ', BmwCar.mro())
print('Inheritance Info : ', BenzCar.mro())
# 결과값:  Inheritance Info :  [<class '__main__.BmwCar'>, <class '__main__.Car'>, <class 'object'>]
# 왼쪽에서 오른쪽으로 읽기 Bmwcar는 car의 자식이고, car는 object class의 자식이다
# 기본적으로 object는 모든 class의 부모임
# 결과값: Inheritance Info :  [<class '__main__.BenzCar'>, <class '__main__.Car'>, <class 'object'>]



### 다중 상속    
class X():
    pass         ##일단 통과해줘 나중에 구현할게. 라는의미


class Y():
    pass


class Z():
    pass


class A(X, Y):   #A가 x와 y 모두를 상속받음
    pass


class B(Y, Z):
    pass


class M(B, A, Z): #M은 B,A, Z 모두를 상속받음
    pass

print(M.mro())
#결과값: [<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, 
# <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, 
# <class 'object'>]            -> A를 상속받음으로 X,Y까지 상속받는셈
print(A.mro())
#결과값: [<class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class 'object'>]



### super().__init()__ 이해    -  상송

# 1) Child 클래스는 Parent 클래스를 상속 받는다. 이는 Child 클래스내에 Parent 클래스의 메소드를 모두 가져오기 하는 것이라고 생각하면 쉽다.
# 2) 그러나 Parent 클래스와 Child 클래스는 모두 __init__()이라는 메소드를 가지고 있다. 따라서 super()를 사용하지 않으면,
#    부모 클래스의 __init__()는 자식 클래스의 __init__()에 의해 overriding(덮어쓰기) 된다.
#     Child 클래스의 __init__() 메소드내에서 super().__init__()을 입력하면 Parent 클래스의 __init__()에 있는 클래스 변수들을 가지고 올 수 있다
# https://velog.io/@gwkoo/%ED%81%B4%EB%9E%98%EC%8A%A4-%EC%83%81%EC%86%8D-%EB%B0%8F-super-%ED%95%A8%EC%88%98%EC%9D%98-%EC%97%AD%ED%95%A0

## super를 쓰지 않은 경우
class Parent:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Child(Parent):
    def __init__(self,c1, p1, p2):
#         super(Child, self).__init__(p1, p2)
        self.c1 = c1
        self.c2 = "This is Child's c2"
        self.c3 = "This is Child's c3"

b= Parent('d', 'e')
a = Child('a', 'b', 'c')
print(b.p1)   ## 출력 : 'd'로 출력됨
print(a.p1)   ## 출력 : 에러  부모 클래스의 p1 인스턴스를 찾지 못함



## super를 활용한 경우
class Parent:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Child(Parent):
    def __init__(self,c1, **kwargs):   ## **kwargs는 dict를 넘기는 것이지만, 여기서 super()의 변수를 넘긴다고 생각하면 된다.
        super(Child, self).__init__(**kwargs)   ## super()는 바로 부모 클래스(여기서는 Parent)를 의미한다. 즉, Parent(Child, self)와 같다.

        self.c1 = c1
        self.c2 = "This is Child's c2"
        self.c3 = "This is Child's c3"

a = Child(p1 = 'a',c1= 'b',p2 = 'c')   ## **kwargs를 썼을 경우에는 이렇게 호출시 p1='a'처럼 지정을 해줘야함(**kwargs가 아닌 경우는 아래에 서술)
a.p1   ## 출력 : 'a'  (부모 클래스의 것을 상속받음)


## super를 활용한 경우2
class Parent:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Child(Parent):
    def __init__(self,c1, **kwargs):   ## **kwargs는 dict를 넘기는 것이지만, 여기서 super()의 변수를 넘긴다고 생각하면 된다.
        super().__init__(**kwargs)   ## super()와 같이 Child를 생략해도 됨.

        self.c1 = c1
        self.c2 = "This is Child's c2"
        self.c3 = "This is Child's c3"

a = Child(p1 = 'a',c1= 'b',p2 = 'c')   ## **kwargs를 썼을 경우에는 이렇게 호출시 p1='a'처럼 지정을 해줘야함(**kwargs가 아닌 경우는 아래에 서술)
a.p1   ## 출력 : 'a'  (부모 클래스의 것을 상속받음)


## **kwargs를 미활용한 경우 (super를 활용한 경우)
class Parent:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

class Child(Parent):
    def __init__(self,c1, p1, p2):
        super(Child, self).__init__(p1, p2)
        self.c1 = c1
        self.c2 = "This is Child's c2"
        self.c3 = "This is Child's c3"

a = Child('a', 'b', 'c')      ## **kwargs를 쓰지 않고 직접 p1, p2 이렇게 지정했을때는 대입값만 써줘도 가능함
                              ## (대입값이 클래스 메소드의 변수 지정 순서대로 대입됨)
a.p1  ## 출력 : 'b  (부모 클래스의 것을 상속받음)



### 파이썬 모듈과 패키지
# 모듈 : 클래스/함수 등을 사용하기 위해 호출할 용도로 쓰이는 파일 
# 패키지: 모듈이 모인것 (파일 트리 구조를 취한 것, 또는 폴더)
# 라이브러리: 외부에서 받아쓰는 패키지를 보통 라이브러리라고함. 패키지와 차이없음

## 상대 경로 패키지
# .. : 부모 디렉토리   - cmd 창에서 cd..은 상위 디렉토리 이동
# .  : 현재 디렉토리   - cmd 창에서 cd.은 현재 디렉토리 이동

### 패키지 폴더내에 __init__.py 파일 생성하기 (파일 안에 내용없어도됨)  
# 용도 : 해당 디렉토리가 패키지임을 선언한다.
# __init__파일이 폴더내 같이 있으면,해당 폴더(디렉토리)의 파일들을 패캐지로 인식
# Python3.x 버젼은 파일이 없어도 패키지 인식함 
# 그래도 python 하위 버전 사용할 경우를 대비하여 호환 위해서 생성하는 것이 안전


# 파일에서 모듈 내 클래스(메소드/속성) 불러오기1
from pkg.fibonacci import Fibonacci   
#from pkg.fibonacci: pkg폴더의 fibonacci 파일에서,'Fibonacci'라는 'class' 호출
Fibonacci.fib(100)   #Fibonacci class 중 fib 메소드 사용

print("ex1 : ", Fibonacci.fib2(200))   #클래스.메소드 사용
print("ex1 : ", Fibonacci().title)     #클래스의 속성 호출, ()를 붙이는 이유는 Fibonacci를 인스턴스화 하기 위해서이다.
 
# 파일에서 모듈 내 클래스(메소드/속성) 불러오기2
from pkg.fibonacci import *    # '*'는 fibonacci 파일 안의 모든 class를 호출

Fibonacci.fib(300)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)

# 파일에서 모듈 내 클래스(메소드/속성) 불러오기3
from pkg.fibonacci import Fibonacci as fb   #Fibonacci를 fb로 명명하여 호출

fb.fib(500)                 #fb로 Fibonacci class의 fib 메소드 호출
print("ex3 : ", fb.fib2(600))
print("ex3 : ", fb().title)

# 파일에서 모듈 내 함수 불러오기1 (모듈에서 함수를 불러올경우 - 모듈 안의 클래스 내 함수가 아닌 모듈 단에서의 함수)
import pkg.calculations as c ##클래스가 아닌 함수를 불러올때는 바로 import 사용
                             ## , 모듈 내 클래스가 있다면 동일하게 from, import 사용하여 클래스 함수/메소드 호출
                             ##이 경우 파일 안의 모든 함수를 불러옴
print("ex4 : ", c.add(10,10))
print("ex4 : ", c.mul(10,4))

# 파일에서 모듈 내 함수 불러오기2 (모듈에서 함수를 불러올경우 - 모듈 안의 클래스 내 함수가 아닌 모듈 단에서의 함수)
from pkg.calculations import div as d #파일 안의 함수 중 div 선택하여 호출
                                      #리소스 절약에 유리 - 강사가 권장함
print("ex5 : ", int(d(100,10)))

# 파일에서 모듈 내 함수 불러오기3 (모듈에서 함수를 불러올경우 - 모듈 안의 클래스 내 함수가 아닌 모듈 단에서의 함수)
import pkg.prints as p
import builtins             #파이썬 기본제공 함수 (굳이 안써도 기본제공됨)

p.prt1()
p.prt2()
print(dir(p))
print(dir(builtins))  #아래는 builtins에서 제공하는 함수, import 안써도 사용가능
#['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 
# 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 
# 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 
# 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
#  'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 
# 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 
# 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 
# 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError',
#  'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 
# 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 
# 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 
# 'OSError', 'OverflowError', 'PendingDeprecationWarning', 
# 'PermissionError', 'ProcessLookupError', 'RecursionError', 
# 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 
# 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning',
#  'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 
# 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 
# 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 
# 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 
# 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', 
# '__doc__', '__import__', '__loader__', '__name__', '__package__', 
# '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint',
#  'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 
# 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 
# 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 
# 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 
# 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 
# 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next',
#  'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 
# 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 
# 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type',
#  'vars', 'zip'] 




### 파일 읽기, 쓰기
# 읽기 모드 r, 쓰기 모드(기존 파일 삭제) w, 추가 모드(파일 생성 또는 추가) a
# 기타 : https://docs.python.org/3.7/library/functions.html#open
# 상대 경로('../', './'), 절대 경로 확인('C:\...')


## 파일 읽기 모드 'r'
#open(경로, 'r'), .close(),  .read(),
# read() : 전체읽기
# read(10) : 문자수 10개 읽기
# readline : 1줄 단위로 읽기 (한번에 전체 안읽음) 
# readlines : 읽어서 리스트 단위로 저장 (1줄마다 1원소로)  
# seek(0,0): 현재 읽고있는 커서 위치를 맨 처음으로 옮김(다 읽었는데 되돌아가야할때)

f = open('./resource/review.txt', 'r')   # '.' 은 현재 디렉터리 의미
contents = f.read()
print(contents)
print(dir(f))
f.close()    # 반드시 close 리소스 반환, 나중에 충돌생김


# 예제2  with문 장점
with open('./resource/review.txt', 'r') as f:  
# f = open('./resource/review.txt', 'r')와 동일한 의미, with를 쓰면
# 자동으로 리소스를 반환하므로 f.close() 할 필요없음
    c = f.read()
    print(iter(c))              #데이터(문자열)를 하나하나 분해함
    print(list(c))
    print(c)

print()

# read : 전체 내용 읽기, read(10) : 10글자 읽기

# 예제3  open함수의 특징과 strip()
with open('./resource/review.txt', 'r') as f:
    for c in f:       #텍스트(문자열) 중 데이터를 한개씩 c에 대입함
        print(c)      #'open' 함수는 데이터 단위를 1줄씩 지정한다는 것을 알수있음
        #print(c.strip())  # 문자열 양쪽 공백 제거 (띄워쓰기 포함)

print()

# 예제4    read 함수의 한계와 seek(0,0)
with open('./resource/review.txt', 'r') as f:
    contents = f.read()
    print('>', contents)  #읽기 완료
    contents = f.read()   
    print('>', contents)  #내용 없음, 위에서 이미 다 읽어 커서가 문장 맨끝에 존재
    f.seek(0, 0)          #f 텍스트의 커서 위치를 다시 처음으로
    contents = f.read()   #읽기 가능
    print('>', contents)



print()

# 예제5 readline()        
with open('./resource/review.txt', 'r') as f:
    line = f.readline()   # readline : 한 줄씩 읽기
    while line:           # readline(문자수) : 문자수 읽기
        print(line, end='')
        line = f.readline()

print()
print()

# 예제6  readlines()
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines() # readlines : 전체 읽은 후 라인 단위 리스트 저장
    print(contents)
    print()
    for c in contents:
        print(c, end='')

print()
print()

# 예제7
with open('./resource/score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line))
    print(score)
    print('Average : {:6.3f}'.format(sum(score) / len(score)))


## 'UTF-8' 타입 리딩 'r' -> 'rt'
# python3 부터는 ANSI 기준으로 작성된 파일만 읽을 수 있다.
# UTF-8로 작성된 파일은 보통 방법으로 읽을 때 에러가 난다.
# 에러내용: UnicodeDecodeError: 'cp949' codec can't decode byte 0xec in position 355: illegal multibyte sequence

# 'rt', encoding='UTF8' 의미 : UTF-8타입으로 되어진 텍스트를 읽는다.
with open('C:/Users/com/python/python_v_test/resource/GL3 HEV 문제점 리스트(0).txt', 'rt', encoding='UTF8') as f:
    c=f.read()
    print(type(c))


## 파일 쓰기 모두 'w' (write)
# write : 지정한 내용 쓰기 (str 타입만 가능)
# writelines : 리스트 -> 파일로 저장
# print('Test Contents!', file=f)  : file 이용하여 프린문으로 쓰기 가능

# 예제1
with open('./resource/test.txt', 'w') as f:
    f.write('niceman!')

# 예제2
with open('./resource/test.txt', 'a') as f:
    f.write('niceman!!')

# 예제3
from random import randint         ##random 파일에서 randint 함수 호출 

with open('./resource/score2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(50, 100))) ##write는 무조건 str 타입으로만 가능함
        f.write('\n')

# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/test2.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Lee\n']
    f.writelines(list)

# 예제5
with open('./resource/test3.txt', 'w') as f:
    print('Test Contents!', file=f)   ##프린트문에서 file을 이용하여 
    print('Test Contents!!', file=f)  ##직접 write 가능



### 파이썬 예외처리

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생 시 예외처리 권장(EAFP 코딩 스타일)

## 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, KeyError
# ZeroDivisionError, AttributeError, FileNotFoundError, Typeerror
# 문법적으로 에러가 없지만 코드 실행 프로세스에서 발생하는 예외 처리 중요

## SyntaxError : 잘못된 문법
# print('test)
# print('Hello'))
# if True
#    pass
# a = 20; b = 30; a+ = b
# x => y


## NameError : 참조 변수 없음
a = 10
b = 15
# print(c)


## ZeroDivisionError : 0 나누기 에러
# print(10 / 0)


# IndexError : 인덱스 범위 오버
x = [10, 20, 30]
# print(x[1])
# print(x[3]) # 예외 발생
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop()) # 예외 발생
# print(x.pop(50)) # 예외 발생


## KeyError
dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul'}
# print(dic['hobby'])     # 키가 존재하지 않으면 예외
# print(dic.get('hobby')) # 안전



## AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외
# print(time.time())  #time에 time 함수 존재하므로 정상동작
# print(time.month()) #time에 month 함수 없으므로 AttributeError
x = [1, 2, 3]
# print(x.append(4))   #list에서 쓰이는 함수이므로 ok
# print(x.add(10))     #list에서 안쓰이는 함수이므로 AttributeError


## ValueError : 참조 값이 없을 때 예외
x = [1, 5, 9]
# x.remove(5) 
# x.remove(100) # 예외 발생
t = (10, 100, 1000)
print(t.index(100))
# print(t.index(7)) # 예외 발생


## FileNotFoundError       # 파일 경로/ 파일명  에러
# f = open('test.txt') # 얘외 발생


## TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
x = [1, 2]
y = (1, 2)
z = 'test'
# print(x + y) # 예외 발생
# print(x + z) # 예외 발생
# print(y + z) # 예외 발생
# print(sum([1,2,3],10,1)) # 예외 발생
# print(x + list(y))
# print(x + list(z)



## 예외 처리 코딩

# try               에러가 발생 할 가능성이 있는 코드 실행
# except 에러명1:    try에서 에러 발생시 except로 진입, 여러개 사용가능(에러 처리)
# except 에러명2: 
# else:             try 블록의 에러가 없을 경우 실행
# finally:          항상 실행

# raise로 예외 상황에 대해 직접 구성 가능
# 에러 처리에 대한 단계적 구성  ex) NameError -> ValueError -> Exception 

# 예제1
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'  # 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except ValueError:          ## try에서 valueError가 발생했을 경우 수행
    print('Not found it! - Occurred ValueError!')
else:                       ## 에러가 없이 try가 정상수행했을 경우 수행
    print('ok! else!')

print()

# 예제2
try:
    z = 'Kim'  # 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except:   #except exception으로도 표기 가능    ## 모든 에러를 처리
    print('Not found it! - Occurred ValueError!')
else:
    print('ok! else!')

print()

# 예제3 (에러 내용 출력)
try:
    z = 'Kim'  # 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! {} in name'.format(z, x + 1))
except Exception as e:         ## 에러 내용을 e로서 명명함
    print(e)                   # 에러 내용 출력
    # pass # 임시로 에러 해결 시 예외 처리
else:
    print('ok! else!')
finally:
    print('ok! finally!')  # 무조건 수행됨 (에러가 있든, 없든)

print()

# 예제4
# 예외처리는 하지 않지만, 무조건 수행 되는 코딩 패턴

try:
    print('try')
finally:
    print('finally')

print()

# 예제5
# 예외 발생 : raise
# raise 키워드로 예외 상황 직접 구성함
# 에러 처리에 대한 단계적 구성  ex) NameError -> ValueError -> Exception

try:
    a = 'Park'
    if a == 'Kim':
        print('Ok! pass')
    else:
        raise NameError     ##예외 상황을 직접 구성함
except NameError:
    print('Raise! Occurred InputError')
except ValueError:
    print('Raise! Occurred ValueError')
except IndexError:
    print('Raise! Occurred IndexError')
except Exception:               # exceotion 전체 예외처리가 맨 뒤에 있어야
    print('Occurred Exception') # valueerror와 indexerror를 먼저 거쳐감                           
else:                           # 그렇지않으면 valueerror도 exception 처리됨
    print('ok! else!')          #exception 맨앞이면,indexerror도 exception처리





## 정규표현식
## import re           re(regular expression) 함수에서 사용 가능
# re.match  /  re.search / re.findall / re.compile(패턴 객체화)
# start() end() span() group() groups()
# or 조건 판단 / 숫자,영문자,한글,특수문자,space,tap,\n 등 판단
# not 조건 판단 / 시작과 끝 조건 판단 / 단축 코드

##re.match (문자열 판단)   시작점부터 판단, 제한적 찾기
import re
re.match('Hello', 'Hello, world!')   # Hello가 있는지 판단
#실행결과: <_sre.SRE_Match object; span=(0, 5), match='Hello'>, span은 존재범위
re.match('Python', 'Hello, world!')
#실행결과: None
re.match('world!', 'Hello, world!')
#실행결과: None           , 뒤에 world가 있으나, match는 처음부터 찾으므로 None


##re.search (문자열 판단)   전체 찾기 : 시작점부터 매칭안되도, 전체구간에서 매칭시킴
re.search('world!', 'Hello, world!') # 시작점부터 매칭안되도, 중간에서 매칭구간 찾음
#실행결과: <re.Match object; span=(7, 13), match='world!'>, 위치 출력 가능


## or 조건으로 문자열 판단(  re.match(A|B),  re.search(A|B) )
re.match('hello|world', 'hello') # hello 또는 world가 있는지 판단
#실행결과<_sre.SRE_Match object; span=(0, 5), match='hello'>


## 범위 판단
# <숫자 판단>
re.match('[0-9]{1,4}', '1234')    #0~9의 숫자가 1개부터 4개까지 존재하는지 판단
#실행결과: <re.Match object; span=(0, 4), match='1234'>
re.match('[0-9]{1,}', '1234')    #0~9의 숫자가 1개이상 존재하는지 판단
#실행결과: <re.Match object; span=(0, 4), match='1234'>
re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-1000-1000')
#실행결과: <_sre.SRE_Match object; span=(0, 13), match='010-1000-1000'>

# <문자 판단>
re.search('[a-z]{1,4}', 'abd1z') #영문 소문자 판단, 영문자는 대소문자 구분함
re.search('[A-Z]{1,4}', 'abd1z') #영문 소문자 판단, 영문자는 대소문자 구분함
re.search('[a-zA-Z]{1,5}', 'ABcd1z') #영문 대소문지 판단
#실행결과: <re.Match object; span=(0, 4), match='ABcd'>, 중간에 1존재하여 끊김
re.match('[가-힣]{1,4}', '클래스GOOD')      #한글 판단
#실행결과: <re.Match object; span=(0, 3), match='클래스'>

#<숫자 + 문자>
re.match('[a-zA-Z0-9]{1,5}', 'ABcd1z') #영문 대소문자 + 숫자 판단
#실행결과: <re.Match object; span=(0, 5), match='ABcd1'>
re.match('[가-힣0-9]{1,7}', '클래스77asb') #한글 + 숫자 판단
#실행결과: <re.Match object; span=(0, 5), match='클래스77'>
re.match('[가-힣a-zA-Z0-9]{1,10}', 'Acd1좋아~good')#한글+영문 대소문자+숫자 판단
#실행결과: <re.Match object; span=(0, 9), match='Acd1좋아'>


# <NOT 조건으로 판단> [^범위]
re.match('[^A-Z]+', 'Hello')  #NOT 영문 대문자. 대문자가 있으므로 패턴에 매칭안됨
re.match('[^A-Z]+', 'hello')  #NOT 영문 대문자. 대문자가 없으므로 패턴에 매칭됨
#실행결과: <_sre.SRE_Match object; span=(0, 5), match='hello'>


# <시작 / 끝 조건 판단하기>   ^[범위]*  ^[범위]+  [범위]*$  [범위]+$
re.search('[^A-Z]+', 'Hello') # +는 시작점에 상관없이 매칭구간 찾음, 대신없으면 return 없음
# 실행결과: <re.Match object; span=(1, 5), match='ello'>
re.search('[A-Z]+', 'hello') #A-Z중 범위로 매칭안되므로 None
# 실행결과:  None - 아예 값이 출력되지 않음, 리턴값 없음
re.search('[A-Z]*', 'hELLO') # *은 첫 시작부터 매칭되지 않으면, 매칭안됨
                             # 그러나, 매칭이 안되도 리턴값 존재 -> span=(0,0)출력
# 실행결과: <re.Match object; span=(0, 0), match=''>

# $ : 끝에 패턴이 매칭되는지 판단
re.search('[0-9]+$', 'Hello1234')    # 끝에 숫자로 끝나는가? -> 숫자로 끝나므로 패턴에 매칭됨
# 실행결과: <_sre.SRE_Match object; span=(5, 9), match='1234'>
re.search('[0-9]+$', 'Hello1234H')   # 끝에 숫자로 끝나는가? -> 숫자로 안끝남, +는 매칭안되면 리턴값없음
# 실행결과 : 리턴값 없음
re.search('[0-9]*$', 'Hello1234H')   # 끝에 숫자로 끝나는가? -> 숫자로 안끝남, *는 match='' 리턴
# 실행결과 : <re.Match object; span=(10, 10), match=''>


# <특수문자 판단>
# 특수 문자를 판단할 때는 특수 문자 앞에 \를 붙임,  ex) \*
# 단, [ ] 안에서는 \를 붙이지 않아도 되지만 에러가 발생하는 경우에는 \를 붙임
print(re.match('[0-9]{4}\([0-9]{3}\)', '1234(111)'))
#실행결과; <re.Match object; span=(0, 9), match='1234(111)'>

print(re.search('\([0-9]{3}\)', '1234(111)'))
#실행결과: <re.Match object; span=(4, 9), match='(111)'>



# <공백 문자(space), tap, \n(줄바꾸기) 판단>
re.match('[a-zA-Z0-9 ]+','Hello 1234')  # 0-9 ]와 같이 띄어쓰기' '로 공백 표현
#실행결과: <_sre.SRE_Match object; span=(0, 10), match='Hello 1234'>
re.match('[a-zA-Z0-9\s]+','Hello 1234') # \s로 공백표현(아래 단축코드 설명 참고)
#실행결과: <_sre.SRE_Match object; span=(0, 10), match='Hello 1234'>
re.match('[a-zA-Z0-9\s\n]+','Hello \n 1234')
#실행결과: <re.Match object; span=(0, 12), match='Hello \n 1234'>

##단축 코드
# \d: [0-9]와 같음. 모든 숫자
# \D: [^0-9]와 같음. 숫자를 제외한 모든 문자
# \w: [a-zA-Z0-9_]와 같음. 영문 대소문자, 숫자, 밑줄 문자
# \W: [^a-zA-Z0-9_]와 같음. 영문 대소문자, 숫자, 밑줄 문자를 제외한 모든 문자
# \s: [ \t\n\r\f\v]와 같음. 공백(스페이스), \t(탭) \n(새 줄, 라인 피드), \r(캐리지 리턴), \f(폼피드), \v(수직 탭)을 포함
# \S: [^ \t\n\r\f\v]와 같음. 공백을 제외하고 \t, \n, \r, \f, \v만 포함


##정규표현식 객체화 함기 (함수처럼 사용하기)
# 매번 정규표현식 패턴 지정하는 것은 비효율적
# 'compile' 함수 사용하여 패턴을 객체화함

p = re.compile('[0-9]{1,}')    # 정규표현식 패턴을 객체로 만듦
p.match('1234')             # 정규표현식 패턴 객체에서 match 메서드 사용
#실행결과: <_sre.SRE_Match object; span=(0, 4), match='1234'>


## re.findall 함수 (패턴에 매칭되는 모든 문자열을 값으로써 list로 출력, index아님)
re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 7 8')
#실행결과: ['1', '2', '4', '7', '8']     # 문자열 값들을 출력함



## 정규표현식으로 찾은 값 활용하기  start() end() span() group()

## start() 함수  
# 매치된 문자열의 시작 위치를 돌려준다
print(re.search('\([0-9]{1,}', '1234(111)').start())
#실행결과: 4


## end()
# 함수 매치된 문자열의 끝 위치를 돌려준다.
print(re.search('\([0-9]{1,}', '1234(111)').end())
#실행결과: 8


## span()
# 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 돌려준다.
print(re.search('\([0-9]{1,}', '1234(111)').span())
#실행결과: (4,8)


## group() 함수 사용하기
# 여러개의 패턴을 한꺼번에 지정하여, 그룹 번호에 해당하는 패턴으로 '값'을 돌려준다
# 정규표현식은 () 괄호로 묶으면 그룹이 됨
m = re.search('([0-9]{1,}) ([0-9]{1,})', '10 295')
m.group(1)    # 첫 번째 그룹(그룹 1)에 매칭된 문자열을 반환
#실행결과: '10'
m.group(2)    # 두 번째 그룹(그룹 2)에 매칭된 문자열을 반환
#실행결과: '295'
m.group()     # 매칭된 문자열을 한꺼번에 반환
#실행결과: '10 295'
m.group(0)    # 매칭된 문자열을 한꺼번에 반환
#실행결과: '10 295'

# groups 함수 사용하기,  결과값을 튜플로 반환함
m.groups()    # 각 그룹에 해당하는 문자열을 튜플 형태로 반환
#실행결과: ('10', '295')

# group에 이름 붙이기     (?P<이름>정규표현식) ->  매치객체.group('그룹이름')
m=re.search('(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(1234)')
m.group('func')    # 그룹 이름으로 매칭된 문자열 출력
#실행결과:'print'
m.group('arg')     # 그룹 이름으로 매칭된 문자열 출력
#실행결과:'1234'




### 파이썬 Excel, CSV 파일 읽기 및 쓰기

# xsl, xlsx 은 엑셀 형식의 파일로 모든 워크시트에 대한 정보 포함됨(서식/수식 등)
            #텍스트 편집기로 열거나 편집불가
# csv는 comma separated values의 약자로 단순히 콤마로 구분해주는 일반 텍스트 형식
    # 대신 서식/수식/매크로 등은 포함안됨, 텍스트 편집기로 호환 가능(확장성 높음)

# CSV : MIME - text/csv

## csv 파일 읽기 / 쓰기 
# csv.reader(), csv.DictReader(), csv.writer(), writerow(), writerows() )

import csv     ##csv 확장자를 컨트롤하기 위한 함수 

# csv 파일 읽기     csv.reader
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader) Header 스킵
    # 확인
    print(reader)  # 문자열이 출력안된고 아래처럼 출력됨
                   # <_csv.reader object at 0x000001CF17A481C0>

    #type을 통해 reader가 지금 어떤 형태인지 확인함
    print(type(reader))  # <class '_csv.reader'> 출력됨, 
                         # 알수없는 타입이나,변수나 리스트 등의 형태로 추측해봄

    print(dir(reader))  # __iter__ 확인됨  ->  반복문으로 사용가능함 확인됨

    for c in reader:
        print(c)

# delimiter 구분자 사용
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|')   ## 구분자 선택
    # next(reader) 사용시 첫줄(내용상 인덱스) 스킵
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ 확인
    print()

    for c in reader:
        print(c)

# Dict 변환    - csv.dictreader(f)
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)    ## 딕셔너리 형태로 읽어들임 ex)(이름, 김정수)
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))  # __iter__ 확인
    print()

    for c in reader:
        for k, v in c.items():  ## 딕셔너리 형태로 출력
            print(k, v)
        print('-----')


## csv 파일 쓰기
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15],[16,17,18]]

with open('./resource/sample3.csv', 'w') as f:  ## sample3.csv 파일 생성됨
    wt = csv.writer(f) # csv.writer: wt라는 쓰기 위한 객체를 생성함
                       # 이 과정에서 쓰는게 아니라, 쓰기위한 대상물 즉 객체를 생성함

    print(dir(wt))     # dir 이용하여 성분/속성 확인 
    print(type(wt))
    for v in w:        # w라는 list에서 1개의 원소씩 꺼내어 write함
        wt.writerow(v)  # writerow: 한줄씩 write 해주는 함수
                        # wt라는 쓰기용 객체를 이용함

# 예제5
with open('./resource/sample3.csv', 'w', newline='') as f:  
    # newline='' 의 의미 : 줄바꿈을 처리하지 않음 -> 
    # 기존에는 with문과 open함수 사용시 중복으로 줄바꿈 처리되어 2줄씩 띄어짐
    # newline=''사용함으로써, OPEN함수에서의 줄바꿈을 없애, WITH문 만으로 줄바꿈
    wt = csv.writer(f)
    # dir 확인
    print(dir(wt))
    print(type(wt))
    for v in w:
        wt.writerow(v)  #writerow: 한줄씩 write 해주는 함수

# 에제6
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15],[16,17,18]]

with open('./resource/sample3.csv', 'w', newline='') as f:
    wt=csv.writer(f)
    wt.writerows(w)    # writerows 한번에 모두 입력하기
                       # writerow 대비 간결하지만, 데이터 필터링하여 쓰기 안됨
                       # writerow는 if 문 등을 사용하여 가능


### pandas를 이용한 엑셀 다루기

# XSL, XLSX : MIME - applications/vnd.excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
# pip install pandas 설치 필요
# pip install xlrd   설치 필요
# pip install openpyxl 설치 필요

# openpyxl, xlsxwriter, xlrd, xlwt, xlutils 등 있으나 pandas를 주로 사용(openpyxl, xlrd) 포함
# 구글에서 pandas excel 검색하면 주요 내용 공부 가능
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html?highlight=excel#pandas.DataFrame.to_excel
import pandas as pd

xlsx = pd.read_excel('./resource/sample.xlsx') # sheetname='시트명' 또는 숫자, header=3, skiprow=1 실습

# 상위 데이터 확인
print(xlsx.head())
print()

# 데이터 확인
print(xlsx.tail())
print()

# 데이터 구조
print(xlsx.shape) # 행, 열


# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False) 
# index는 첫번째 열에 숫자를 붙이는 것으로, 쓰지 않고 싶을떄는 false




%는 Magic Command라는 기능으로, 파이썬 문법이 아닌 쥬피터 노트북(Ipython)이나 colab과 같은 커널에서만 자체적으로 제공하는 내장 함수

#https://sosomemo.tistory.com/60

 %matplotlib inline, %matplotlib notebook
: 원래 %matplotlib 은 matplotlib 의 backend 를 설정하는 명령어
%matplotlib -l 을 입력하면 여러개의 선택지가 나옴
그렇지만 보통 Jupyter Notebook 에서는 inline, notebook 을 많이 사용함
(%matplotlib inline	show 명령 없이도 바로 그래프 표현 (정적), show 명령 없이도 바로 그래프 표현 (동적))

%time, %timeit, %%time, %%timeit
: 수행된 시간을 측정하여 반환해주는 매직 커맨드




### Python의 바이트 문자열과 유니코드  ###


## encode와 decode 함수

#https://wikidocs.net/10501

#컴퓨터에 저장하려면 먼저 인코딩해야합니다. 즉, 바이트로 변환해야 한다는 뜻입니다.
#음악을 저장하려면 먼저 MP3, WAV 등을 사용하여 음악을 인코딩해야합니다. 그림을 저장하려면 PNG, JPEG 등을 사용하여 먼저 인코딩해야합니다.
#텍스트를 저장하려면 먼저 ASCII, UTF-8 등을 사용하여 텍스트를 인코딩해야합니다. MP3, WAV, PNG, JPEG, ASCII 및 UTF-8이 인코딩의 예입니다.
#인코딩은 오디오, 이미지, 텍스트 등을 바이트 단위로 나타내는 형식입니다.
#파이썬에서 바이트 문자열은 b'abcd'와 같이 나타내며 내부적으로는 인간이 읽을 수 없는 인코딩된 일련의 바이트들 입니다.


'I am a string'.encode ('ascii')  # 출력 : b'I am a string'

'I am a string'.encode ('utf-16') # 출력 : b'\xff\xfeI\x00 \x00a\x00m\x00 \x00a\x00 \x00s\x00t\x00r\x00i\x00n\x00g\x00'

b'\xff\xfeI\x00 \x00a\x00m\x00 \x00a\x00 \x00s\x00t\x00r\x00i\x00n\x00g\x00'.decode('utf-16')  # 출력 : I am a string


import binascii
binascii.hexlify(b'I am a string') # 출력 : b'4920616d206120737472696e67'


## hex() 함수

http://pythonstudy.xyz/python/article/515-%EC%A0%95%EC%88%98---HexString-%EB%B3%80%ED%99%98

# 정수를 16진수 문자열(Hex)로 변환하기
i = 123
hexStr = hex(i)
print(hexStr)  # '0x7b'

# 문자를 ASCII 16진수 문자열(Hex)로 변환하기
# : 영문자에 대한 ASCII 코드는 ord() 함수를 사용하여 구할 수 있다.
# : 예를 들어, 문자 'A'에 대한 ASCII 코드는 ord('A') 를 사용하여 65를 구할 수 있다.
a = hex(ord('A'))
print(a)  # '0x41'

# 16진수 문자열(Hex)을 정수로 변환하기
# : 16진수 문자열을 정수로 변환하기 위해서는 int() 라는 내장함수를 사용할 수 있다.
# : int() 함수의 첫번째 파라미터에는 16진수 문자열을 지정하고, 두번째 파라미터에는 이 문자열이 16진수(hexadecimal)로 되어 있음을 표시하는 16을 넣으면 된다.
hexStr = '0x7b'
i = int(hexStr, 16) # 16진수로 해석
print(i)  # 123 출력



## wave 확장자 오디오 파일을 읽어보기

search_str = b'\x54\x48\x49\x53'  # 0x54 가 아니라, x54x48 이런식으로 표현되므로, 찾을 정규표현 문자도 이와 같이 표현함

with open('/content/gdrive/MyDrive/대회/한국어 AI 경진대회 회의 음성/예선/Q1/문제1-5.wav', 'rb') as f:
      byte = f.read()
      print(byte)  # b'RIFFJ\x16\x03\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x80>\x00\x00\x00}\x00\x00\x02\x00\x10\x00data6\xf5\x01  ~~
                   # 위와 같이 0x16이 아니라, x16으로 표현됨.... (유의하자)

byte.find(search_str)  # 출력 : 128354

