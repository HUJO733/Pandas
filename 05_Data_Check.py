import pandas as pd

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
# print(df)

# DataFrame 확인
# '''
# describe : 계산 가능한 데이터에 대해 컬럼별로
# 갯수, 평균, 표준편차, 최소/최대값 등의 정보 보여줌
# '''
# df = df.describe()
# print(df)

# info : 데이터 타입, 용량등의 정보 보여줌
# df = df.info()
# print(df)

# 처음 n개의 row 반환 / 기본값 5
# df = df.head(3)
# print(df)

# 마지막 n개의 row 반환 / 기본값 5
# df = df.tail(4)
# print(df)

# df = df.values

# index의 값과 데이터 확인
# df = df.index
# print(df)

# 컬럼 확인
# df = df.columns
# print(df)

# row, column 갯수
# df = df.shape
# print(df)


# Series 확인
# print(df['키'].describe())
# print(df['키'].min())
# print(df['키'].max())
# print(df['키'].nlargest(3)) # 큰 값 순서대로 n개
# print(df['키'].mean()) # 평균
# print(df['키'].sum())
# print(df['키'].count())
# print(df['학교'].unique()) # 중복 제외한 데이터
# print(df['학교'].nunique()) # 중복 제외한 데이터의 갯수