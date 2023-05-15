from bs4 import BeautifulSoup
import pandas as pd
import urllib.request as req
import requests
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'}
Data=pd.DataFrame()
for i in range(1,27):
            url="https://m.stock.naver.com/api/json/sise/dailySiseIndexListJson.nhn?code=KOSPI&pageSize=200&page="+str(i)
            data = requests.get(url,headers=headers)
            value= data.json()   
            kospi = value['result']['siseList']
            df=pd.DataFrame(kospi)
            df=df[['cd','dt','ov','ncv','cv','cr']] #특정 열 선택
            df = df.rename(columns={'cd':'code',"dt":"date",'ov':'open','ncv':'close','cv':'diff','cr':'rate'}) #열 이름 변경
            Data=pd.concat([Data,df])
            #index를 reset해주고, 인덱스 열을 버린다.
            Data=Data.reset_index(drop=True)
print(Data)
print(Data.isna().sum())