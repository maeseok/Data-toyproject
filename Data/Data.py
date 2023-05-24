import pandas as pd
import matplotlib.pyplot as plt
SP=pd.read_csv("SP500.csv")
KS=pd.read_csv("KOSPI.csv")
DW=pd.read_csv("DOW.csv")
NS=pd.read_csv("NASDAQ.csv")
df= pd.DataFrame({'Date':KS['date'],'SP':SP['close'],'KOSPI':KS['close'],
                  'DW':DW['close'],'NS':NS['close']})
#inplace를 통해 기존의 인덱스(숫자)를 대체
df.set_index('Date',inplace=True)
df=df.dropna()
df=df.corr()
print(df)

