from bs4 import BeautifulSoup
import pandas as pd
import urllib.request as req
import requests
df=[]

symb=[]
xymd=[]
open=[]
close=[]
diff=[]
rate=[]
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'}
for i in range(1,520):
            url="https://finance.naver.com/world/worldDayListJson.naver?symbol=NAS@IXIC&fdtc=0&page="+str(i)
            data = requests.get(url,headers=headers)
            value= data.json()         
            for j in range(len(value[0])):
                symb.append(value[j]["symb"])
                xymd.append(value[j]["xymd"])
                open.append(value[j]["open"])
                close.append(value[j]["clos"])
                diff.append(value[j]["diff"])
                rate.append(value[j]["rate"])
            df=pd.DataFrame({"code":symb, "date":xymd,"open":open,"close":close,
                                  "diff":diff,"rate":rate})
print(df)
print(df.isna().sum()) 