import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Graph Style
import mplcyberpunk
plt.style.use('cyberpunk')

def readData(name):
    return pd.read_csv(name+".csv")

def madeData(name):
    value=readData(name)
    temp = pd.DataFrame({'Date':KS['date'],name:value['close'],'KS':KS['close']})
    #inplace를 통해 기존의 인덱스(숫자)를 대체
    temp.set_index('Date',inplace=True)
    temp = temp.dropna()
    return temp

def showChart(df):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15,6))
    #numpy 다차원 배열 공간을 1차원으로 평탄화해주는 함수 
    ax_li = axes.flatten()
    df_cols = df.columns
    for i, (col, ax) in enumerate(zip(df_cols, ax_li)):
        print(col,ax)
        ax.plot(df[col], linewidth=0.8)
        ax.set_title(col)

    plt.tight_layout()
    plt.show()

KS=readData("KS")
KDW = madeData("DW")
showChart(KDW)
#KSP = madeData("SP")
#showChart(KSP)
#KNS = madeData("NS")
#showChart(KNS)
