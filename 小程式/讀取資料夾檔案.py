import os

path = '/Users/leeyu/Downloads/新增包含項目的檔案夾/'
file_list = os.listdir(path)
# print(type(file_list))

for i in file_list:
    print(i)