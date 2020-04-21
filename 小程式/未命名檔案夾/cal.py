# pip install pandas
import pandas as pd
import time
import threading

# c=a-b
a = ['',
    '',
    '']
b = ['',
    '',
    '']

# 存擋名稱，不給路徑預設存在和程式相同資料夾
c = ['',
    '',
    '']


s_ = time.time()
def cal(a, b, c):
    s11 = time.time()
    print('讀取 '+a+'...')
    a1 = pd.read_csv(a, header=None, skip_blank_lines=False)
    print('讀取 '+b+'...')
    b1 = pd.read_csv(b, header=None, skip_blank_lines=False)
    e1 = time.time()
    print('讀取時間: ', e1-s11)

    c1 = a1 - b1

    s3 = time.time()
    c1.to_csv(c, header=False, index=False, encoding="utf-8")
    e3 = time.time()
    print(c +' 存檔時間: ', e3-s3)

threads = []
for i in range(3):
    threads.append(threading.Thread(target=cal, args=(a[i], b[i], c[i])))

for i in threads:
    i.join()

e_ = time.time()
print('全部處理完成，總時間: ', e_-s_)