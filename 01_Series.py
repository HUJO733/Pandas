# Pandas : 2차원 데이터
# Series : 1차원 데이터 (정수, 실수, 문자열 등)

import pandas as pd

# Series 객체 생성
temp = pd.Series([-20, -10, 10, 20], index=['1월','2월','3월','4월'])

# print(temp)
# print(temp['4월']) # 해당 인덱스의 위치나 값을 넣어도 출력 가능

