# 함수 적용하기 apply

import pandas as pd

# excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')

# '키'에 cm 붙이기
def add_cm(height):
    return str(height) + 'cm'

df['키'] = df['키'].apply(add_cm)
# print(df)

# 'SW특기' 첫글자만 대문자로
def capitalize(lang):
    if pd.notnull(lang): # NaN 이 아닌지 확인
        return lang.capitalize()
    return lang

# df['SW특기'].str.capitalize() 를 함수화

df['SW특기'] = df['SW특기'].apply(capitalize)
print(df)
