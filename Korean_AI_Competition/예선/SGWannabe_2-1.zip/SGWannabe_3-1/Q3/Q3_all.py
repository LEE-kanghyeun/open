#https://github.com/marsbroshok/VAD-python
import warnings

from vad import VoiceActivityDetector
# -*- coding: utf-8 -*-
import os

from scipy.io import wavfile
import noisereduce as nr
import json
from collections import OrderedDict
import numpy as np

warnings.filterwarnings(action='ignore')

path = "/Q3/DataSet/Q3/"

path_noise_reduce = "/Q3/DataSet/Q3/NoiseReduce/"

org_path = os.getcwd()

print(org_path)

file_list = os.listdir(org_path+path)
print(file_list)
all_json_list = []
for fname in sorted(file_list):
    try:
        # 노이즈 제거
        print(fname)
        rate, data = wavfile.read(org_path+path+fname)
        reduced_noise = nr.reduce_noise(y=data, sr=rate)
        only_fname = os.path.splitext(fname)[0]
        wavfile.write(os.path.expanduser(org_path+path_noise_reduce+only_fname+"_noise.wav"), rate, reduced_noise)

        # 유효구간 추출
        v = VoiceActivityDetector(org_path+path_noise_reduce+only_fname+"_noise.wav")
        #v.plot_detected_speech_regions()
        raw_detection = v.detect_speech()
        speech_labels, speech_valid_duration_speech_begin, speech_valid_duration_speech_end = v.convert_windows_to_readible_labels(raw_detection)

        begin_data = np.trunc(speech_valid_duration_speech_begin[0] * 1000) / 1000
        end_data = np.trunc(speech_valid_duration_speech_end[-1] * 1000) / 1000

        one_data = {'filename': fname, 'begin': begin_data, 'end': end_data}
        print(one_data)
        all_json_list.append(one_data)
    except:
        pass

json_result = OrderedDict()
json_result["Q3"] = "Q3"

# 파일이름: [참가팀명.json], UTF-8 encoding
json_result["Q3"] = all_json_list
with open(org_path+'/Q3/SGWannabe_Q3.json', 'w', encoding='UTF-8-sig') as file:
    file.write(json.dumps(json_result, ensure_ascii=False))