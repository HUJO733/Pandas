# 데이터 선택 (iloc) : 위치를 이용해서 원하는 row에서 원하는 col 선택

import pandas as pd

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')

# 0번째 위치의 데이터
# print(df.iloc[0])

# 0~4번째 위치의 데이터
# print(df.iloc[0:5])

# 0번째 위치의 1번째 데이터
# print(df.iloc[0, 1])

# 0, 1번째 위치의 2번째 데이터
# print(df.iloc[[0, 1], 2])

# 0, 1번째 위치의 3, 4번째 데이터
# print(df.iloc[[0,1], [3,4]])

# 0~4번째 위치의 3~7번째 데이터
print(df.iloc[0:5, 3:8])
