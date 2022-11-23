# -*- coding: utf-8 -*-
import os
import librosa
import sys
import numpy as np
import json
from collections import OrderedDict

#python Q1.py "DataSet/Q1/문제1-5.wav"
file_path_and_name = sys.argv[1]

duration = librosa.get_duration(filename=os.path.expanduser(file_path_and_name))

# 실행 파일
fname = os.path.basename(file_path_and_name)
print(fname)

#소수점 셋째자리까지 버림하여 실수 형식으로 작성
print(duration)
result_duration = np.trunc(duration*1000)/1000
print(result_duration)

#THIS 청크 검색
search_str = b'\x54\x48\x49\x53'

all_json_list = []
json_result = OrderedDict()
json_result["Q1"] = "Q1"
#파일이름: [참가팀명.json], UTF-8 encoding

with open(file_path_and_name, 'rb') as f:
    byte = f.read()

# THIS 세션 플래그 위치 달기
this_chuck_position_start = byte.find(search_str)
if this_chuck_position_start > 0:
    one_data = {'filename': fname, 'THIS': this_chuck_position_start, 'duration': result_duration}
else:
    one_data = {'filename': fname, 'duration': result_duration}

all_json_list.append(one_data)
json_result["Q1"] = all_json_list
with open('SGWannabe_Q1.json', 'w', encoding='UTF-8-sig') as file:
    file.write(json.dumps(json_result, ensure_ascii=False))