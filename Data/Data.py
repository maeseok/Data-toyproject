import pandas as pd
import matplotlib.pyplot as plt
import scipy

def readData(name):
    return pd.read_csv(name+".csv")

def madeData(name):
    value=readData(name)
    temp = pd.DataFrame({'Date':KS['date'],name:value['close'],'KS':KS['close']})
    #inplace를 통해 기존의 인덱스(숫자)를 대체
    temp.set_index('Date',inplace=True)
    temp = temp.dropna()
    return temp

def LinearReg(Data,code):
    if code=="SP":
        x=Data.SP
    elif code=="DW":
        x=Data.DW
    else:
        x=Data.NS
    y=Data.KS
    #단순 선형회귀분석 및 시각화
    model = scipy.stats.linregress(x,y)
    #단순선형회귀식
    regr_line = f'Y = {model.slope:.2f}*x+{model.intercept:.2f}'
    #시각화 단계
    plt.figure(figsize=(7,7))
    plt.plot(Data[code],Data['KS'],'.')
    plt.plot(Data[code],model.slope*Data[code]+model.intercept,'r')
    plt.legend([code +"& KS", regr_line])
    plt.xlabel(code)
    plt.ylabel('KS')
    plt.show()
    
KS=readData("KS")
KSP = madeData("SP")
KDW = madeData("DW")
KNS = madeData("NS")
LinearReg(KSP,"SP")
LinearReg(KDW,"DW")
LinearReg(KNS,"NS")
#KSP.corr()
#KDW.corr()
#KNS.corr()



#df= pd.DataFrame({'Date':KS['date'],'SP':SP['close'],'KOSPI':KS['close'],
#                  'DW':DW['close'],'NS':NS['close']})

