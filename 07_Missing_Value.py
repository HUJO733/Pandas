# 결측치 : 비어있는 데이터

import pandas as pd
import numpy as np

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')

# NaN 데이터를 '없음'으로 채움 fillna
# print(df.fillna('없음'))

# '학교' 데이터 전체를 NaN으로 설정
# df['학교'] = np.nan
# print(df)
# print(df.fillna('모름')) # NaN 데이터 '모름'으로 채움
# print(df['SW특기'].fillna('확인 중')) # SW특기 데이터 중에서 NaN에 대해서 적용


# 데이터 제외하기 dropna
# 전체 데이터 중에서 NaN을 포함하는 데이터 삭제
# print(df.dropna())


# axis : index(row) or columns
# how : any(하나라도 포함시) or all(전부가 NaN일 경우)
print(df.dropna(axis='index', how='any'))