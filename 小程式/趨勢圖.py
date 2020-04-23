import matplotlib.pyplot as plt
import pandas as pd
import datetime

df = pd.read_excel('/Users/leeyu/OneDrive/NCU.xlsx')
# d109 = pd.DataFrame()
# d109[0], d109[1] = df['d'][2:], df['i'][2:]
# d108 = pd.DataFrame()
# d108[0], d108[1] = df['s'], df['y']

plt.figure(figsize=(16, 8), dpi=200)

x1 = pd.to_datetime(df.loc[2:6, 2], format="%m/%d", errors='ignore')#.dt.strftime("%m/%d")
y1 = df.loc[2:6, 7]
x2 = pd.to_datetime(df.loc[2:22, 17], format="%m/%d", errors='ignore')#.dt.strftime("%m/%d")
y2 = df.loc[2:22, 23]
x3 = pd.to_datetime(df.loc[2:17, 39], format="%m/%d", errors='ignore')#.dt.strftime("%m/%d")
y3 = df.loc[2:17, 42]
x4 = pd.to_datetime(df.loc[2:16, 44], format="%m/%d", errors='ignore')
y4 = df.loc[2:16, 47]

plt.plot(x1, y1, 'bo-', label='109')
plt.plot(x2, y2, 'ro-', label='108')
plt.plot(x3, y3, 'yo-', label='107')
plt.plot(x4, y4, 'go-', label='106')
plt.xlabel('Date')
plt.ylabel('ranking')
plt.title('CS')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.grid()

for x, y in zip(x1, y1):
    if type(x) == pd._libs.tslibs.nattype.NaTType:
        continue
    plt.text(x, y + 3, str(y), ha='center', va='bottom', fontsize=8)

for x, y in zip(x2, y2):
    plt.text(x, y + 3, str(y), ha='center', va='bottom', fontsize=8)

for x, y in zip(x3, y3):
    plt.text(x, y + 3, str(y), ha='center', va='bottom', fontsize=8)

for x, y in zip(x4, y4):
    plt.text(x, y + 3, str(y), ha='center', va='bottom', fontsize=8)


plt.show()