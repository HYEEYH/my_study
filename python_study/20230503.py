# 5월 3일 ---------------------------------------------------
# 구글 코렙에서 보는게 더 자세함.
# 수업1
# 선형대수학 복습
# 방정식
# 벡터


# 파이썬 심화 복습
# args 와 파이썬 심화

## python basic p.230
## - 문) add_all 함수 만들어보기
## add_all(1,2,3,4,5,6,7,8,9,10)
## (힌트) *args를 input으로 받기
print("add_all 함수를 짜보기")
# def add_all(*inputs):
#     a = 0
#     for i in range(len(inputs)):
#         a += inputs[i]
#     return a

# print(add_all(1,2,3,4,5,6,7,8,9,10))
# # ++++++++++++ 오류 난다고 하는데 왜 안나지...>??
print("\n")








# Numpy 복습

# 어레이 안에 있는 각각이 전부 객체(object)가 된다
# 리스트보다 집어 넣는것은 느리지만 꺼내 쓰는것은 빠름.(각각 따로 쓸 수 있어서)
# array 실습
print("array 실습")
import numpy as np
# print(np.__version__)  # 넘피 버전 확인하기
print("\n")










# 플래튼
# reshape
# transpose







# T operation
# 슬라이싱도 가능
# 브로드캐스팅 가능

## 문제2) 0~20까지 숫자의 배열을 만든 다음 arr1에는 짝수
##      arr2는 홀수가 들어간 배열을 출력해보기
print("array 문2")

# import numpy as np

# arr = np.arange(0,21)
# arr1 = []
# arr2 = []
# for i in arr:
#   if arr[i] % 2 == 0:
#     arr1.append(arr[i])
#   else:
#     arr2.append(arr[i])

# print(arr1)
# print(arr2)
print("\n")

# # 위의 코드와 동일한 코드

# import numpy as np
# Arr = np.arange(0,21)

# Arr1 = Arr[Arr%2==0]
# Arr2 = Arr[Arr%2!=0]

# print(Arr)
# print(Arr1)
# print(Arr2)
print("\n")




# 불리안배열
# 정수배열을 사용한 인덱싱


# 유니버셜 함수
# 이항 유니버셜 함수

#통계 메소드

# 기타 메소드
# where
# x if 조건 else y의 벡터화 버전
# numpy를 사용하여 배열을 빠르게 처리할 수 있으며 다차원도 간결하게 표현이 가능.#
# sort() : array의 sort에서는 내림차순, 오름차순을 선택하는 옵션이 없다.(->리스트의 sort와 다른점)

# 선형대수 패키지
# 단위행렬
# 대각원소가 1이고 나머지는 0인 n차 정방행렬을 말함
# numpy의 eye()함수를 사용하여 만들 수 있다
# 사용방법
# import numpy as np
# identity = np.eye(4)
# print(identity)

# 대각행렬 :대각 성분 이외의 모든 성분이 모두 0인 n차 정방행렬
# dot : 원소간의 곱(element-wise product). 벡터의 내적(행렬의 곱) 곱해서 더하는걸 내적이라고 함.
# matmul : matrix multiplication









# 수업5 ------------------------------------------------------
# pandas
# 분석용 라이브러리
# 넘피 위에서 돌아감
# 설치를 원할경우
#!pip install numpy  # 느낌표를 쓴 이유는 리눅스에서는 이렇게 해야 돌아가는데 코렙은 리눅스
#!pip install pandas
# 슬라이싱가능
# 멀티인덱스 접근방법
# - obj[[1,3,5]] : [[]] 이렇게 대괄호 두번 써주기
# integer location based(iloc): 아이록. 정수 기반 접근
# obj.iloc[1:4]
# obj.loc['a':'c']
# loc은 라벨로 접근하는거
# iloc은 integer로 접근하는거임
# 결과는 같아 보이지만 암튼 뭔가 다름. 데이터 분석할떄 달라짐.

# 데이터프레임
# import numpy as np
# df = pd.DataFrame(np.arange(24).reshape(4,-1), columns = ['c1','c2','c3','c4','c5','c6'], index=['r1','r2','r3','r4'])
# df['c3']  # df의 c3은 뭐니?
# 또는
# df.c3

# c1, c3 열을 가져오고 싶을때 : df[['c1','c3']]  # 멀티인덱스를 써야 오류 안남
# df['r1':'r2']   # r1에서 r2까지 가져와라
# df['c1':'c2']   # 이건 왜 값이 안나올까??
# -> 컴퓨터는 열 중심으로 읽음
# r1에서 r2로 갈때는 데이터가 안끊김.(위에서부터 열을 따라가면서 내려다보면서 읽을때)
# (0.1.2.3.4.5.6.7.8.9.0.11)까지 전부 읽을 수 있음.
# 그런데!
# c1에서 c2로 갈때 데이터가 중간에 끊김 (위에서부터 열을 따라가며 내려다보며 읽을때 )
# (0,6,12,18 읽고 그 뒤에 아무것도 없어서 못읽음. c2 처음으로 다시 못올라감)



# 판다스 설치안되서 안될듯
# 근데 vs코드에서는 맨 뒤 인코딩 빼도 된다고 함.
# import pandas as pd

# stock = pd.read_csv('https://raw.githubusercontent.com/Youngpyoryu/Lecture_Note/main/%ED%8C%8C%EC%9D%B4%EC%8D%AC/stock_2020_01.csv', encoding= 'CP949')




# import pandas as pd
# stock = pd.read_csv('/content/stock_2020_01.csv',encoding='CP949')
# stock

# stock.head() # 위에서 5개 읽기
# 5개 아니고 개수 다르게 읽고싶으면 ()안에 숫자 넣기
# stock.tail()  # 밑에서 5개 읽기



# 기술통계량
# stock.describe()
# 위에서부터

# 개수
# 평균
# 표준편차
# 최소값
# 데이터의 25%값
# 데이터의 50%값(중앙값) median = 50%
# 데이터의 75%값
# 최대값

# np.mean(A)  # 평균
# np.median(A)  # 중앙값
# # 결측치 있나 확인하는 방법
# stock.isna()

#stock.isna().sum()  # 더해서 확인하는게 더 편함
# 이거는 결측치 없음.
# 또는
#stock.isnull.sum()


## 주의 () 빼먹으면 컴퓨터 상으로 연산은 하지만 출력은 안함.
## 아까 sort도 마찬가지. ()빼면 함수만 호출했지 적용을 안한거임.


# 데이터의 자료형이 뭔지 궁금할때
# info()
# stock["kospi"].sort_values()  # 값에따라 정렬. 값이 높은거->낮은거
# unique
# 중복되는 값을 제거하고 유일한 값만 담고있는 Series를 반환.
# 시리즈만 됨.


# obj.unique()
# Series밖에 안됨. 데이터 프레임에서는 안됨.
# But!!
# 데이터프레임에서 시리즈를 만든다면 유니크 사용할 수 있음.

# Value_counts
#.value_counts()
# .value_counts(normalize=True) : 
# frame.sort_index(axis=1)
# axis=1 열로 인식/ 0이면 행으로 인식
# 판다스와 넘피가 반대로 돌아감

# - map : Series의 각각의 element들을 다른 어떤 값으로 대체하는 역할
# - apply: map보다 적용할 수 있는 범위가 더 큼

"실습"
# def sub_custom_value(x,val):
#   return x-val

# s.apply(sub_custom_value,args=(10,))  
# # 주의사항 : 10 뒤에 (10, )처럼 가변공간을 줘야함.

# def add_custom_values(x,**kwargs):
#   for month in kwargs:
#     x += kwargs[month]
#   return x

# s.apply(add_custom_values, june=30, july=20, august=25)  
""

# # 답이 이상하게 나옴.10씩 세번 돌아가며 더해짐.
# # 원래 데이터에 month가 없는데 억지로 넣으면 일단 돌아가긴 하는데 답이 이상하게 나옴
# # 원래 데이터를 바꿀 수 없음.(kwarge는 딕셔너리만 받을 수 있음. 딕셔너리는 수정 불가)
# # 함수 쓸 때 주의하기!