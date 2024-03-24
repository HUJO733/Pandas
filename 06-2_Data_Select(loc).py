# 데이터 선택 (loc) : 이름을 이용해서 원하는 row에서 원하는 col 선택

import pandas as pd

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')

# 해당 row의 전체 데이터
# print(df.loc['1번'])

# 해당 index의 가져오고 싶은 데이터
# print(df.loc['1번', '국어'])

# 여러개의 index의 가져오고 싶은 데이터
# print(df.loc[['1번', '2번'], '국어'])

# 여러개의 index의 가져오고 싶은 여러 데이터
# print(df.loc[['1번', '2번'], ['국어', '영어']])

# 슬라이싱 활
# 기존 슬라이싱과의 차이점 : 콜론 뒤의 값 포함됨
print(df.loc['1번':'5번', '국어':'사회'])