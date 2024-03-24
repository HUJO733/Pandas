import pandas as pd

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')

# 컬럼 선택
# print(df['이름'])
# print(df[['이름', '키']])

# 컬럼 선택(정수 index)
# print(df.columns[0])

# print(df[df.columns[0]]) # 해당 index 컬럼에 해당하는 데이터


# 슬라이싱
# print(df['영어'][0:5])
# print(df[['이름', '키']][:3])
# print(df[3:]) # 모든 컬럼