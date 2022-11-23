# -*- coding: utf-8 -*-
import os
import librosa
import sys
import numpy as np
import json
from collections import OrderedDict

data_path = "/Q1/DataSet/Q1/"
org_path = os.getcwd()

print(org_path)
file_list = os.listdir(org_path+data_path)
all_json_list = []

#THIS 청크 검색
search_str = b'\x54\x48\x49\x53'

for fname in sorted(file_list):
    print(fname)
    #소수점 셋째자리까지 버림하여 실수 형식으로 작성
    duration = librosa.get_duration(filename=org_path+data_path+fname)

    # 소수점 셋째자리까지 버림하여 실수 형식으로 작성
    print(duration)
    result_duration = np.trunc(duration * 1000) / 1000
    print(result_duration)

    with open(org_path+data_path+fname, 'rb') as f:
        byte = f.read()

    # THIS 세션 플래그 위치 달기
    this_chuck_position_start = byte.find(search_str)
    if  this_chuck_position_start > 0:
        one_data = {'filename': fname, 'THIS' : this_chuck_position_start, 'duration': result_duration}
    else:
        one_data = {'filename': fname, 'duration': result_duration}

    all_json_list.append(one_data)

json_result = OrderedDict()
json_result["Q1"] = "Q1"
json_result["Q1"] = all_json_list
with open(org_path+'/Q1/SGWannabe_Q1.json', 'w', encoding='UTF-8-sig') as file:
    print(json_result)
    file.write(json.dumps(json_result, ensure_ascii=False))