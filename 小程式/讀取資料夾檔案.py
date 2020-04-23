import os
import re
import pandas as pd

def main():
    path = '/Users/leeyu/Downloads/新增包含項目的檔案夾/'
    file_list = os.listdir(path)
    # print(type(file_list))  # list

    # Track_name = re.compile(r'')
    # Artist_name = re.compile(r'')
    # Playlist_name = ''

    # csv_content = []
    df = pd.DataFrame(file_list)

    df.to_csv('list.csv')

 

# test
main()


# for i in os.walk('/'):
#     print(i)

# for i in os.listdir(path):
#     for j in os.listdir(path+'\\'+i):
#         print(path+'\\'+i+'\\'+j)


