# 그룹화 하기
# 동일한 값을 가진 것들끼리 합쳐서 통계 또는 평균 등 값을 계산하기 위해 사용

import pandas as pd

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')

# # '학교'의 데이터가 '북산고'인 데이터만 가져오기
# df = df.groupby('학교').get_group('북산고')
# print(df)


# # 각 그룹의 데이터 갯수 size
# print(df.groupby('학교').size())

# # '학교' 그룹의 '능남고' 데이터 갯수
# print(df.groupby('학교').size()['능남고'])

# '학교'로 그룹화한 결과의 '키' 평균값
# print(df.groupby('학교')['키'].mean())


# 학년 추가
df['학년'] = [3,2,3,1,1,3,2,2]

print(df.groupby(['학교','학년']).sum())
