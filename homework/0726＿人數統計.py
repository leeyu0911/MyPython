'''
從106年1月到107年5月每個月人口總數如下：
[8397. 8393. 8389. 8376. 8378. 8395. 8411. 8409. 8406. 8413. 8408. 8408. 8414. 8421. 8411. 8392. 8404.]
資料也可以用以下方式表示：
[8397,8393,8389,8376,8378,8395,8411,8409,8406,8413,8408,8408,8414,8421,8411,8392,8404]
接著請您：
1.利用迴圈跑出17個月各月的總人數
2.請計算出這17個月的人口平均值、中位數、最大值與最小值。
'''

import numpy as np

num_pepple = [8397, 8393, 8389, 8376, 8378, 8395, 8411, 8409, 8406,
              8413, 8408, 8408, 8414, 8421, 8411, 8392, 8404]

month = 1
year = 106
# for n in num_pepple:
#     if month > 12:
#         year += 1
#         month = 1
for i, j in enumerate(num_pepple):
    print(i, j)
    print(f'民國{year + i // 12}年{month + i % 12}月總人數：{j}')

np_people = np.array(num_pepple)
print('平均值：', np.mean(np_people).round(2))
print('中位數：', np.median(np_people))
print('最大值：', np.max(np_people))
print('最小值：', np.min(np_people))