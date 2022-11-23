# https://ponyozzang.tistory.com/440?category=800537
# https://blog.naver.com/yejin7676/221990720703



### 파일 복사
import shutil
src = r'C:\Users\'
dst = r'C:\Users\'  ## 파일이 존재한다면 덮어쓰기됨
shutil.copyfile(src, dst)

### 확장자 변경하여 파일 복사
src = r'C:\Users\복사본.txt'
dst = r'C:\Users\복사본.xml'  ## 파일이 존재한다면 덮어쓰기됨
shutil.copyfile(src, dst)


import time
time.sleep(5)




### 파일 삭제
# import os
# os.remove(r"C:\Users\6509504\Desktop\test_folder\test_file_copy_delete - 복사본2.txt")

### 파일이 존재하는지 확인하고 삭제
import os
file=r"C:\Users\복사본2.txt"
if os.path.isfile(file):
    os.remove(file)


### 확장자 조건부 파일 삭제
import os
import glob
for f in glob.glob(r'C:\Users\Desktop\test_folder\*.xml'):    ## glob을 활용하여 확장자 xml 파일만 삭제
    os.remove(f)




### 폴더 생성 - mkdir
import os
path = r'C:\Users\Desktop\test_folder\newfolder'   ## 중간에 경로가 없으면 에러 발생, 이미 폴더가 존재하는 경우에도 에러 발생 (if문 활용 필요)
os.mkdir(path)

### 재귀적 폴더 생성  - makedirs
import os
path = r'C:\Users\Desktop\test_folder\newfolder111\new'  ## 중간에 경로가 없어도 폴더를 만들며, 경로를 생성함, 이미 있는 경우에는 에러 발생 (if문 활용 필요)
os.makedirs(path)


### 폴더 삭제
# import os
# os.rmdir("./test3")  ## 폴더 안에 파일이 하나도 없는 경우에는 삭제가 가능하지만 파일이 하나라도 있는 경우에는 에러가 발생

### 폴더 삭제 2
# import shutil
file=r"C:\Users\Desktop\test_folder2"
if os.path.isfile(file):
    shutil.rmtree(r"C:\Users\Desktop\test_folder2")  ## 폴더 안에 파일이 있으면 파일까지 같이 삭제, 경로 없으면 에러(if랑 같이 쓰자)



## 오래된 파일 (14일 경과) 삭제 예제    :   https://blog.naver.com/wideeyed/221797721352
import os
from datetime import datetime

def delete_old_files(path_target, days_elapsed):
    """path_target:삭제할 파일이 있는 디렉토리, days_elapsed:경과일수"""
    for f in os.listdir(path_target): # 디렉토리를 조회한다
        f = os.path.join(path_target, f)
        if os.path.isfile(f): # 파일이면
            timestamp_now = datetime.now().timestamp() # 타임스탬프(단위:초)
            # st_mtime(마지막으로 수정된 시간)기준 X일 경과 여부
            is_old = os.stat(f).st_mtime < (timestamp_now - (days_elapsed * 24 * 60 * 60))   ### 마지막으로 수정한 시간과 기준 시간 비교
            if is_old: # X일 경과했다면
                try:
                    os.remove(f) # 파일을 지운다
                    print(f, 'is deleted') # 삭제완료 로깅
                except OSError: # Device or resource busy (다른 프로세스가 사용 중)등의 이유
                    print(f, 'can not delete') # 삭제불가 로깅
path = r'C:\Users\Desktop\test_folder\newfolder'
days_elapsed = 180   ## 180일 경과시 삭제
delete_old_files(path, days_elapsed)


