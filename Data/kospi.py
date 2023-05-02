from bs4 import BeautifulSoup
import pandas as pd
import urllib.request as req
import requests
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.62'}
for i in range(1,20):
            url="https://m.stock.naver.com/api/json/sise/dailySiseIndexListJson.nhn?code=KOSPI&pageSize=200&page="+str(i)
            data = requests.get(url,headers=headers)
            value= data.json()           
            kospi = value['result']['siseList']
            df=pd.DataFrame(kospi)
print(df)