# 조건에 해당하는 데이터 선택

import pandas as pd

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')

# 키가 185 이상인지 여부 True / False
# print(df['키'] >= 185)

# 키가 185 이상인 데이터
# filt = (df['키'] >= 185)
# print(df[filt])

# ~ : filt에 해당되지 않는 데이터
# print(df[~filt])

# 키가 185 이상인 데이터의 수학 데이터
# print(df.loc[df['키'] >= 185, '수학'])

# 키가 185 이상인 데이터의 이름, 수학, 과학 데이터
# print(df.loc[df['키'] >= 185, ['이름','수학','과학']])

# 키가 185 이상이고 학교가 북산고인 데이터 (AND 조건)
# print(df.loc[(df['키'] >= 185) & (df['학교'] == '북산고')])

# 키가 170보다 작거나 200보다 큰 데이터 (OR 조건)
# print(df.loc[(df['키'] < 170) | (df['키'] > 200)])

# '송'으로 시작하는 이름 startswith
# filt = df['이름'].str.startswith('송')
# print(df[filt])

# '태'라는 글자가 들어가는 이름 contains
# filt = df['이름'].str.contains('태')
# print(df[filt])
# '태'라는 글자가 안들어가는 이름
# print(df[~filt])

# SW특기가 'Python' 이거나 'Java'인 데이터 isin
# langs = ['Python','Java']
# filt = df['SW특기'].isin(langs)
# print(df[filt])

# SW특기를 소문자로 바꾸고 비교
# langs = ['python','java']
# filt = df['SW특기'].str.lower().isin(langs)
# print(df[filt])

# na : NaN 데이터 설정
filt = df['SW특기'].str.contains('Java', na=False)
print(df[filt])