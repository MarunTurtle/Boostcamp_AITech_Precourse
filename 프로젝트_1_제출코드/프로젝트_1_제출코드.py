# -*- coding: utf-8 -*-
"""(공통)_1차시_프로젝트_1_제출코드.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qn0wwbJSoahx71gYrOnVnrTC7TVbLS4J

### [TODO] 코드 실행 : 가상환경 설치하기

가상환경 설치를 완료하고, 현재 파이썬 버전을 확인해보세요.
"""

import sys
print(sys.version)

"""### [TODO] 코드 구현 : 실행환경 점검 - 파일 입출력

압축 파일 내에 제공된 'zen of python.csv' 파일을 불러와 내용을 출력해보세요.
불러올 파일을 저장한 변수명은 'df_csv' 입니다.
"""

import pandas as pd

## 코드시작 ##

df_csv = pd.read_csv('zen of python.csv')

## 코드종료 ##

print(df_csv)

"""### [TODO] 코드 구현 : 간단한 코드 작성하고 실행하기 (numpy)

다음 지시문의 코드를 작성하고 결과를 출력해보세요.
"""

pip install numpy
import numpy as np

# 주어진 리스트
data = [10, 25, 40, 55, 70]

## 코드시작 ##
# 1. numpy 배열로 변환하여 출력하세요.

arr = np.array(data)
print("Numpy array:", arr)

# 2. 리스트의 모든 원소의 합을 계산하여 출력하세요.

sum_data = np.sum(arr)
print("Sum:", sum_data)

# 3. 리스트의 모든 원소의 평균을 계산하여 출력하세요.

mean_data = np.mean(arr)
print("Mean:", mean_data)

# 4. 리스트의 최댓값과 최솟값을 출력하세요.

max_data = np.max(arr)
min_data = np.min(arr)
print("Max:", max_data)
print("Min:", min_data)

# 5. 각 원소를 10으로 나누는 연산을 수행하고 결과를 출력하세요.

divided_by_10 = arr / 10
print("Divided_by_10:", divided_by_10)

# 6. 각 원소를 3으로 거듭제곱하는 연산을 수행하고 결과를 출력하세요.
cubed = np.power(arr, 3)
print("Cubed:", cubed)

## 코드종료 ##

"""ALL RIGHTS RESERVED. ⓒNAVER Connect Foundation."""