# 데이터 정렬

import pandas as pd

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')

# '키' 기준 오름차순 정렬
# print(df.sort_values('키')) # 전체 데이터 출력
# print(df['키'].sort_values) # '키'의 데이터만 출력
# 내림차순
# print(df.sort_values('키', ascending=False))

# 수학, 영어 점수 기준 오름차순
# (먼저 나온 수학이 기준 동순위에서 영어로 비교)
# print(df.sort_values(['수학', '영어']))

# index 기준으로 정렬
print(df.sort_index())