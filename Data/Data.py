import lxml
from collections import OrderedDict
import pandas as pd

def getYFHistDataMonthly(code: str, year: int, month: int) -> pd.DataFrame:
    response = getResponseYFHistDataMonthly(code, year, month)
    tree = lxml.html.fromstring(response.text)
    table = tree.find_class("W(100%) M(0)")[0]  # history 테이블 요소 찾기
    
    # 테이블 칼럼명 가져오기
    column_names = []
    thead = table.find("thead")
    tr = thead.find("tr")
    th = tr.findall("th")
    for head in th:
        span = head.find("span")
        column_names.append(span.text)
    column_names = [x.replace('*', '') for x in column_names]  # 특수문자(*) 지워주기
    
    # 테이블 모든 행 정보 가져오기
    tbody = table.find("tbody")
    tr = tbody.findall("tr")
    data_list = list()
    for row in tr:
        data = OrderedDict()
        td = row.findall("td")
        for idx, elem in enumerate(td):
            span = elem.find("span")
            data[column_names[idx]] = span.text.replace(',', '')  # 쉼표 제거
        data_list.append(data)
        
    # 데이터프레임 생성
    df = pd.DataFrame(data_list)
    
    # 자료형 변경
    df["Date"] = pd.to_datetime(df["Date"], format="%b %d %Y")
    df["Open"] = df["Open"].astype(float)
    df["High"] = df["High"].astype(float)
    df["Low"] = df["Low"].astype(float)
    df["Close"] = df["Close"].astype(float)
    df["Adj Close"] = df["Adj Close"].astype(float)
    df["Volume"] = df["Volume"].astype(float)
    
    # 날짜 오름차순으로 정렬
    df.sort_values(by="Date", ascending=True, inplace=True, ignore_index=True)
    
    return df