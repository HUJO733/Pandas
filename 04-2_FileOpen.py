import pandas as pd

# csv 파일 열기
# df = pd.read_csv('score.csv')
# print(df)

# 지정 갯수만큼의 row를 건너뜀
# df = pd.read_csv('score.csv', skiprows=1)
# print(df)

# 지정 row 제외
# df = pd.read_csv('score.csv', skiprows=[1,3,5])
# print(df)

# 지정 갯수만큼의 row를 가져옴
# df = pd.read_csv('score.csv', nrows=4)
# print(df)

# 2 row 건너뛴 후 4 row 가져옴
# df = pd.read_csv('score.csv', skiprows=2, nrows=4)
# print(df)


# txt 파일 열기
# sep을 설정하지 않을 경우 데이터가 연결돼서 나옴
# df = pd.read_csv('score.txt', sep='\t')
# print(df)

# index 컬럼 지정
# df = pd.read_csv('score.txt', sep='\t', index_col='지원번호')
# '''
# 이걸 풀어서 쓰면
# df = pd.read_csv('score.txt', sep='\t')
# df.set_index('지원번호')
# '''
# print(df)


# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)