# -*- coding: utf-8 -*-
import os
import json
import re
import sys
from collections import OrderedDict

def preprocessing(origninal):
    ms = re.findall('\(([^)]+)', origninal)
    origninal = origninal.replace('*','').replace('+','').replace('u/','').replace('l/','').replace('o/','').replace('n/','').replace('b/','').replace('/','').replace('(','').replace(')','')
    if len(ms) > 0:
        #print(ms[0])
        for i in range(len(ms)):
            if i%2 == 0:
                origninal = origninal.replace(ms[i],'',1)

    return origninal

#python Q2.py "DataSet/answer.json"
file_path_and_name = sys.argv[1]

q2_question = []
all_json_list = []
json_result = OrderedDict()
json_result["Q2"] = "Q2"
with open(os.path.expanduser(file_path_and_name)) as json_file:
    json_data = json.load(json_file)
    q2 = json_data['Q2']
    for q2_data in q2:
        print("original : "+ q2_data['original'])
        #q2_question.append(q2_data['original'])
        result = preprocessing(q2_data['original'])
        print("new : "+result)
        one_data = {'original': q2_data['original'], 'new': result}
        all_json_list.append(one_data)

json_result["Q2"] = all_json_list
#파일이름: [참가팀명.json], UTF-8 encoding
with open('SGWannabe_Q2.json', 'w', encoding='UTF-8-sig') as file:
    file.write(json.dumps(json_result, ensure_ascii=False))
# df = pd.DataFrame(q2_question, columns=['original'])
# print(df.original.str.extract('(([0-9]?[0-9]?[0-9]?[0-9]))'))