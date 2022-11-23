# -*- coding: utf-8 -*-
#github 소스 참고 (MIT 라이센스) https://github.com/marsbroshok/VAD-python
import warnings
from vad import VoiceActivityDetector
from scipy.io import wavfile
import noisereduce as nr
import os
import sys
import json
from collections import OrderedDict

warnings.filterwarnings(action='ignore')

#python Q3.py "DataSet/Q3/문제3-1.wav"
if len(sys.argv) > 1:
    file_path_and_name = sys.argv[1]


path = os.path.split(file_path_and_name)[0]+"/"
path_noise_reduce = path+"/NoiseReduce/"
# 실행 파일
fname = os.path.basename(file_path_and_name)
print(fname)


# 노이즈 제거
print(fname)
rate, data = wavfile.read(os.path.expanduser(path + fname))
reduced_noise = nr.reduce_noise(y=data, sr=rate)
only_fname = os.path.splitext(fname)[0]
wavfile.write(os.path.expanduser(path_noise_reduce + only_fname + "_noise.wav"), rate, reduced_noise)

# 유효구간 추출
v = VoiceActivityDetector(os.path.expanduser(path_noise_reduce + only_fname + "_noise.wav"))
# v.plot_detected_speech_regions()
raw_detection = v.detect_speech()
speech_labels, speech_valid_duration_speech_begin, speech_valid_duration_speech_end = v.convert_windows_to_readible_labels(
    raw_detection)
one_data = {'filename': fname, 'begin': speech_valid_duration_speech_begin[0],
            'end': speech_valid_duration_speech_end[-1]}
print(one_data)

all_json_list = []
json_result = OrderedDict()
json_result["Q3"] = "Q3"

# 파일이름: [참가팀명.json], UTF-8 encoding
all_json_list.append(one_data)
json_result["Q3"] = all_json_list
with open('SGWannabe_Q3.json', 'w', encoding='UTF-8-sig') as file:
    file.write(json.dumps(json_result, ensure_ascii=False))