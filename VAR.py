import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def readData(name):
    return pd.read_csv(name+".csv")

def madeData(name):
    value=readData(name)
    temp = pd.DataFrame({'Date':KS['date'],name:value['close'],'KS':KS['close']})
    #inplace를 통해 기존의 인덱스(숫자)를 대체
    temp.set_index('Date',inplace=True)
    temp = temp.dropna()
    return temp

KS=readData("KS")
KSP = madeData("SP")
KDW = madeData("DW")
KNS = madeData("NS")

fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(15,6))
df = pd.concat([
    yf_kakao[['Adj Close', 'Volume']],
    yf_naver[['Adj Close', 'Volume']],
    yf_samsung[['Adj Close', 'Volume']],
    yf_skhy[['Adj Close', 'Volume']],], axis=1)

df.columns = [
    'kakao_ac', 'kakao_v', 
    'naver_ac', 'naver_v', 
    'samsung_ac', 'samsung_v', 
    'skhy_ac', 'skhy_v'
]
ax_li = axes.flatten()
df_cols = df.columns
for i, (col, ax) in enumerate(zip(df_cols, ax_li)):
    ax.plot(df[col], linewidth=0.8)
    ax.set_title(col)

plt.tight_layout()
plt.show()