# 데이터 수정

import pandas as pd

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')

# '학교' 컬럼의 데이터 수정(북산고 → 상북고, 능남고 → 무슨고)
# print(df['학교'].replace({'북산고 ':'상북고', '능남고':'무슨고'}))

# 'SW특기' 컬럼의 데이터 소문자로 변경 (대문자는 lower 대신 upper)
# print(df['SW특기'].str.lower())

# '학교' 컬럼의 데이터에 텍스트 데이터 추가
# print(df['학교'] + '등학교')

# # 컬럼 추가('총합' 이라는 컬럼명으로 추가)
# df['총합'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']
# # '결과' 라는 컬럼 추가 후 Fail 데이터 저장
# df['결과'] = 'Fail'
# # '총합'이 400보다 큰 데이터의 '결과'를 'Pass'로 업데이트
# df.loc[df['총합'] > 400, '결과'] = 'Pass'

# 컬럼 삭제
# print(df.drop(columns=['총합']))
# print(df.drop(columns=['국어', '영어', '수학']))

# row 삭제
# print(df.drop(index='4번'))

# filt = df['수학'] < 80
# print(df[filt]) # '수학'이 80 미만인 데이터 출력 
# print(df.drop(index=df[filt].index)) # 위 데이터 삭제


# row 추가
# df.loc['9번'] = ['이정환','해남고',184,90,90,90,90,90,'Kotlin']
# print(df)

# '4번'의 'SW특기'를 'Python으로 변경
# df.loc['4번', 'SW특기'] = 'Python'
# print(df)

# '5번'의 '학교'와 'SW특기'를 변경
# df.loc['5번', ['학교','SW특기']] = ['능남고', 'C']
# print(df)


# # 컬럼 순서 변경
# cols = list(df.columns)
# # print(cols)
# df = df[[cols[-1]] + cols[0:-1]] # 가장 마지막 컬럼을 맨 앞으로 
# print(df)


# # 컬럼 이름 변경
# df.columns = ['Name','School','Height','Object1','Object2','Object3','Object4','Object5','SW']
# print(df)