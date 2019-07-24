# 讀取CSV文件表頭
# with open('test.csv', 'r', encoding='utf8') as f:
#     h = f.readline()
#     h.split(',')
#
#     for i in h.replace('\ufeff','').split(','):
#         print(i)

import requests
import json

url = 'http://opendataap2.penghu.gov.tw/resource/files/2019-03-08/74a2fac1bb86fe3050fd3fbbc952bda3.json'
r = requests.get(url)
dict_data = json.loads(r.text)  # dict_data = r.json()

for i in dict_data:
    print("{\ufeff工作計畫_科目名稱}, {補助事項或用途}, {補助對象}".format(**i))


# 寫入dict_data
with open('data.json', 'w', encoding='utf8') as j:
    j.write(str(dict_data))