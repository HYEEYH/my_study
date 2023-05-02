# 5월 2일 수업1 ------------------------------------------------
# 함수
# 스왑해보기

print("함수 스왑 연습하기")
# def swap_value(x,y):
#     temp = x
#     x = y
#     y = temp

# def swap_offset(offset_x, offset_y):
#     temp = a[offset_x]
#     a[offset_x] = a[offset_y]
#     a[offset_y] = temp

# def swap_reference(list, offset_x, offset_y):
#     temp = list[offset_x]
#     list[offset_x] = list[offset_y]
#     list[offset_y] = temp

# a = [1,2,3,4,5]
# swap_value(a[1], a[2])
# print(a)

# swap_offset(1,2)
# print(a)

# swap_reference(a,1,2)
# print(a)
print("\n")






print("함수 만들기 연습하기")
# 두개의 숫자를 input으로 받으면 앞의 숫자를 뒤의 숫자로 나누는 함수
# 나눗셈을 한 후에는 몫과 나머지 순으로 튜플 값을 반환한다.

### 나의 풀이:
# def div(a,b):
#     a = int(input("숫자입력1: "))
#     b = int(input("숫자입력2: "))
#     num1 = a//b
#     num2 = a%b
#     tuple_1 = (num2, num1)
#     print(tuple_1)
print("\n")


### 해설 강사님 강의자료- 파이썬 베이직 225p :
### 두개의숫자를 input으로 받으면 작은수로 큰수를 나는 목과 나머지를 반환하는 함수.
### 반환값은 튜플로 되어있으며 몫, 나머지 순으로 되어있다
### 단, 0으로 나누는것은 불가. 두 수 중 작은수가 0이라면 화면에 0은 사용할수 없다를 출력하고 종료되어야 한다
# def div3(a,b):
#     if a<b:
#         big = b
#         samll = a
#     elif b<=a:
#         big = a
#         small = b
#     else:
#         print("정수가 아닙니다")
#     if small == 0:
#         print("0은 사용할 수 없습니다.")
#     elif abs(big)<0 or abs(small)<0:
#         print("정수를 입력해주세요")
#     else:
#         q = big//small
#         r = big%small
#         return(q,r)
print("\n")





# 매개변수가 몇개가 필요할지 모를 때 : *args 사용
# 매개변수에 *args를 붙이면 함수가 받은 input 모두를 tuple로 묶어줌.
# 매가변수가 몇개인지 모를때 : **kwargs 사용


## 파이썬 베이직 229p
## 어떠한 string을 받으면 일정한 단위로 끊어서 화면에 출력하는 함수를 만들기
## 끊는 단위는 따로 정하지 않으면 2로 설정한다.
print("함수 만들기 연습하기 - args 사용")

## 나의 풀이
# def add(**kwargs):
#     string1 = input("문장을 입력하세요:")


## 문제 해설
# def func(string, unit=2):
#     i = 0
#     while i < len(string):
#         print(string[i:i+unit])
#         i += unit
print("\n")





## 파이썬 베이직 230p
## add_all 함수 짜보기
## add_all(1,2,3,4,5,6,7,8,9,10)   ->답: 55
## 힌트) args 로 받은 후에 리스트로 다시 받아서 만들기
print("함수 만들기 연습하기 - args 사용2")

# def add_all(*inputs):
#     s = 0
#     for i in range(len(inputs)):
#         s += inputs[i]
#     return s

# def add_all2(*inputs):
#     return sum(inputs)

# def add_all3(*args):       
#     s = 0
#     for i in args:
#         for j in i:
#             a += j
#         return s
    
# add_all(1,2,3,4,5,6,7,8,9,10)
# add_all3(1,2,3,4,5,6,7,8,9,10)


# def add_all4(*args):
#     temp = 0
#     for i in range(len(args)):
#         if type(args[i]) == list:
#             for j in args[i]:
#                 temp += j
#         else:
#             temp += args[i]
#     return temp
# add_all4(1,2,3,4,5,6,7,8,9,10)
print("\n")







## 파이썬 베이직 239p
## 팩토리얼 구하기
## 1부터 시작해서 어떤 범위에 있는 모든 정수 곱하기
print("함수 만들기 연습하기 - 팩토리얼 구하기")

## 나의 풀이
# a = int(input("정수입력1: "))
# i = 0
# for i in range(a):
print("\n")





## 파이썬 베이직 242p
## 대기번호**번 : 사람이름  출력하는 함수 만들기
## 사람 이름으로 되어있는 리스트를 받아서 "대기번호##번:사람이름"을 화면에 출력하고
##(번호표, 사람이름)을 원소로 이루어진 리스트를 반환하기
print("함수 만들기 연습하기 - 리스트반환1")

# people = ["펭수", "뽀로로", "뚝딱이", "텔레토비"]

# def fun1(line):
#     new_line = []
#     i = 1              # 대기번호를 트래킹 하는 변수 i 
#     for x in line:
#         print("대기번호 %d번 : %s" %(i, x))
#         new_line.append((i, x))
#         i += 1         # 별도로 업데이트 해 줘야 함.
#     return new_line

# lines = func1(people)
print("\n")







# enumerate(열거하다)
# 반복 가능한 객체의 인덱스와 원소에 함께 접근 할 수 있는 함수.

# lst = ['a', 'b', 'c']
# for x in enumerate(lst):
#   print(x)
print("\n")



print("함수 만들기 연습하기 - 리스트반환2: 리스트반환1과 같은 결과")

# people = ['펭수','뽀로로','뚝딱이','텔레토비']

# def func1(line):
#     new_lines = []
#     for idx,val in enumerate(line):
#         print('대기번호 %d번 : %s' %(idx,val))
#         new_lines.append((idx+1,val))
#     return new_lines
print("\n")








### zip()
### - 반복가능한 객체들을(2개이상) 병렬적으로 묶어주는 함수
### - 각 원소들을 튜플의 형식으로 묶어줌



### lamda
### 파이썬3에서는 사용권장되지 않으나
### 데이터분석에선 많이 쓰임.
### 단점 : 변수를 1개밖에 못받음. map함수를 이용하여 묶어줘야 함

print("람다 함수 연습1")
# func2 = lambda x : x+2
# c = func2(2)
# print(c)
print("\n")

print("람다 함수 연습2")
# items = [1,2,3,4,5]
# squared_map = list(map(lambda x : x**2, items))
# print(squared_map)
print("\n")


print("람다 함수 연습문제 - p. 251")
# 람다와 맵을 이용하여 items의 요소들을 strin(문자)로 바꾸기
# items = [1,24,3,6,7]
# str_items = list(map(lambda x:str(x),items))
# print(str_items)
print("\n")




### 파이썬 베이직 자료 p.255
## 구구단 2단을 list comprehension을 이용하여 구현하고 리스트를 화면에 출력해보기
## 나의풀이
# li_1=[]
# for i in range(1,10):
#     li_1.append(i*2)
#     print(li_1)
print("\n")





# p.258
# for 문 + if 문
# 10부터 20까지 짝수만 담은 리스트를 만들어보기
print("for 문 + if 문 연습")
# list3 = []
# for x in range(10, 21):
#   if x % 2 == 0:
#     list3.append(x)
# print(list3)


# # 또는


# lc_2 = [x for x in range(10,21) if x%2==0]
# print(lc_2)
print("\n")






## p.258
## 1부터 10의 제곱수 중 50 이하인 수만 리스트에 저장하기










#수업 5 -----------------------------------------------------------

# 빅데이터를 위한 선형대수학
# 다양한 학문의 기초
# 방정식을 푸는것



# Numpy
# numerical python의 약자.
# 산술계산용 라이브러리


# 행렬 계산해보기
#  5, 6            1, 2
#  7, 8            3, 4


### Ndarray vs list
print("Ndarray vs list")


# import time
# start = time.time()    #시작시간 저장
# python_list = [x**3+10 for x in python_list]
# print("time:", time.time() - start)   #현재시각 - 시작시간 = 실행시간




## 강의자료- 파이썬 넘피 - 43p
## 로또 번호 생성기 만들기

print("로또 번호 생성기 만들기")
# -> 코드랩 확인





