import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Graph Style
import mplcyberpunk
plt.style.use('cyberpunk')

def readData(name):
    return pd.read_csv(name+".csv")

def madeData(name,df):
    temp = pd.DataFrame({'Date':KS['date'],name:df['close'],'KS':KS['close']})
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
    
#정상성 분석 함수
def adf_test(data):
    data = pd.read_csv(data+".csv")
    from statsmodels.tsa.stattools import adfuller
    #axis=1은 열을 의미한다.
    #data = data.drop(['code'],axis=1) 
    data=data[['date','close']]
    #로그 변환 - 주가가 큰 폭으로 움직여서
    data['close']=np.log(data['close'])
    print(data)
    result = adfuller(data['close'])
    #print(f'원 데이터 ADF Statistic: {result[0]:.3f}')
    #print(f'원 데이터 p-value: {result[1]:.3f}')
    if(result[1]>0.05):
        #차분으로 추세제거
        data['close']=data['close'].diff(periods=1).iloc[1:]
        data=data.dropna()
        result = adfuller(data['close'])
        #print(f'1차 차분 ADF Statistic: {result[0]:.3f}')
        #print(f'1차 차분 p-value: {result[1]:.10f}')
    #변환 후 반환
    return data
#그레인저 인과검정
def granger(df,data,data2):
    from statsmodels.tsa.stattools import grangercausalitytests
    df_cols = df.columns
    maxlag=14
    #KS->DW
    df_outs=grangercausalitytests(df[[data,data2]],maxlag=maxlag)
    print(df_outs)
    
    #DW->KS
    df_outs=grangercausalitytests(df[[data2,data]],maxlag=maxlag)
    print(df_outs)
    
KS=adf_test("KS")
DW=adf_test("DW")
KDW = madeData("DW",DW)
granger(KDW,"KS","DW")
#showChart(KDW)
#granger(KDW)
#KSP = madeData("SP")
#showChart(KSP)
#KNS = madeData("NS")
#showChart(KNS)