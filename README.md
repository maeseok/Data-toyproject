# 한국증시와 미국증시 상관관계 분석 및 예측

## 📋 프로젝트 개요
한국 증시(KOSPI, KOSDAQ)와 미국 증시(S&P 500, NASDAQ 등)의 상관관계를 분석하여 양국 시장 간의 연관성과 영향을 시각적으로 탐구합니다.

## 🔍 주요 흐름
1. **데이터 수집 및 전처리**: 네이버 크롤링을 통한 한국 및 미국 증시 데이터 수집
2. **상관관계 분석**: Pearson, Spearman 등 다양한 상관계수 분석
3. **회귀 분석**: 전제조건인 선형성, 독립성, 정규성, 등분산성, 다중공선성을 확인한 후 회귀 분석
4. **선행 연구 분석**: 한국 증시, 미국 증시 관계에 대한 논문 및 연구 분석
5. **시계열 분석**: Granger 인과검정, ADF test, 공적분 검정 등 진행 
6  **다변량 시계열 모델 적용**: ARCH, VAR, VECM 적용 
7  **결과 보고**: 상관관계 및 분석 결과 요약  

## 📊 사용된 데이터
- **기간**: 2012년 07월 19일 ~ 2023년 06월 23일
- **지표**:
  - 한국: KOSPI
  - 미국: S&P 500, NASDAQ, Dow Jones

## 🛠️ 기술 스택
- **언어**: Python
- **라이브러리**: 
  - 데이터 분석: Pandas, NumPy
  - 시각화: Matplotlib, Seaborn, Plotly
  - 통계 분석: SciPy, Statsmodels
- **데이터 수집**: bs4, requests

## 📂 폴더 구조
```
📁 프로젝트 루트
├── 📁 Data                # 원본 및 전처리된 데이터 저장소
├── 📄 사이트.txt           # 분석 방법론 및 학습 내용
└── 📄 README.md           # 프로젝트 설명 파일
```

## 📈 주요 결과
1. **상관관계 결과**:
  ![image](https://github.com/user-attachments/assets/7285762d-21e2-4f85-83d1-ef81987db2b6)
  대체적으로 한국 증시와 미국 증시는 약 0.8의 상관계수를 갖는다.

2. **결과 보고**:
  ![image](https://github.com/user-attachments/assets/a34118bb-26fd-444d-99cd-c0b40a8071a4)
  최종적으로 시계열 분석과 선행 연구 조사를 통해 VECM 모델을 사용해 10개 지점에 대한 예측 결과이다.
  [분석 링크](https://blog.naver.com/mae_seok/223144765209)
  
3. **배운 점**:
  해당 분석을 통해 선형성과 비선형성에 따라 Pearson, Spearman의 상관관계 분석을 수행할 수 있으며,
  또한 시계열 분석에 있어 추세, 계절성, 주기와 정상성 검정, 공적분 관계 등의 조건을 확인하며
  통계적 분석에 입각한 데이터 분석을 수행할 수 있었다.  
  

  


