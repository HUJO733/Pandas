# Index : 데이터에 접근할 수 있는 주소값

import pandas as pd

data = {
    '이름' : ['채치수','정대만','송태섭','서태웅','강백호','변덕규','황태산','윤대협'],
    '학교' : ['북산고','북산고','북산고','북산고','북산고','능남고','능남고','능남고'],
    '키' : [197,184,168,187,188,202,188,190],
    '국어' : [90,40,80,40,15,80,55,100],
    '영어' : [85,35,75,60,20,100,65,85],
    '수학' : [100,50,70,70,10,95,45,90],
    '과학' : [95,55,80,75,35,85,40,95],
    '사회' : [85,20,75,80,10,80,35,95],
    'SW특기' : ['Python','Java','JavaScript','','','C','PYTHON','C#']
}

df = pd.DataFrame(data, index=['1번','2번','3번','4번','5번','6번','7번','8번'])

# print(df.index)

# index 이름 설정
# df = df.index.name = '지원번호'
# print(df)

# index 초기화 → 지원번호라는 인덱스 이름이 일반컬럼이 됨
# df = df.reset_index()
# print(df)

# index 삭제(inplace : 실제 데이터에 바로 반영)
# df = df.reset_index(drop=True, inplace=True)
# print(df)

# index 설정
df = df.set_index('이름')
# print(df)

# index 정렬
# df = df.sort_index() # 기본값 오름차순
# df = df.sort_index(ascending=False) # 내림차순 설정
print(df)