# 4월 25일 1 -------------------------------------------------------------------------

##       <<      실      습      >>
## 문제1)다음 함수를 정의하기
##      정수 n을 입력받고, n보다 작은 수 중 3의 배수와 5의 배수를 모두 더한 합을 반환하는 함수
##      함수 이름 : sum_3_5
##      파라미터 : 
##      반환값 : 

print("def 연습문제 1")
# def sum_3_5(n):             #+++++++++++++++++++++++++++ 안돌아가!@
#     if n > a and n > b:
#         for i in range(n):
#             a = 3*n
#         for j in range(n):
#             b = 5*n
#         print(a+b)
#         return a+b
print("\n")

print("def 연습문제 1 - 해설1")
# def sum_3_5(n):
#     result = 0
#     for i in range(n):                   # 아니면 range(1,n)
#         if i % 3 == 0 or i % 5 == 0:
#             result += i
#     return result
print("\n")

print("def 연습문제 1 - 해설2")  # 틀림
# def sum_3_5(n):
#     result = 0
#     for i in range(n):      # 3의 배수이면서 5의배수가 있을때(예시: 15) 두번 계산된다.
#         if i % 3 == 0:
#             result += i
#         if i % 5 == 0:      # -->> if 대신 elif 쓰면 됨.
#             result =+ i
#     return result
print("\n")








##       <<      실      습      >>
## 문제2)다음 함수를 정의하기
##      정육면체 주사위 2개가 있다.
##      2개의 주사위를 던졌을 때 나올 수 있는 주사위 눈의 조함을 모두 print하는 함수를 정의하기
##      함수 이름 : double_dice
##      파라미터 : 
##      반환값 : 
##      출력 예시))
##      1, 2
##      6, 3

print("def 연습문제 2")
# def double_dice():               #+++++++++++ 오류남
#     n1 = [1,2,3,4,5,6]
#     n2 = [1,2,3,4,5,6]
#     for i in range(n1):
#         for j in range(n2):
#             print("i", "j")   
# double_dice()   
print("\n")


print("def 연습문제 2 - 해설1") 
# def double_dice():
#     for i in range(1,7):               # 범위 1~6
#         for j in range(1,7):           # 범위 1~6
#             print(i,j)
# double_dice()                          #####   ++++++++++++++++ 함수를 정의한 후에는 호출을 해 줘야 출력 된다! 까먹지 말기!
print("\n")

print("def 연습문제 2 - 해설2") 
# def double_dice():
#     i = 1
#     while i < 7:
#         j = 1
#         while j < 7:
#             print(i, j)
#             j += 1
#         i += 1
# double_dice()
print("\n")








##       <<      실      습      >>
## 문제3) 두 수의 차이를 구하는 함수
##      함수에 입력된 두 정수의 차이를 계산하고 반환하는 함수를 정의하기
##      함수 이름 : get_diff
##      파라미터 : a, b
##      반환값 : result()

print("def 연습문제 3") 
# def get_diff(a, b):
#     result = a - b
#     return result
# get_diff(6,2)
print("\n")

print("def 연습문제 3 - 해설1") 
def get_diff(a, b):
    result = abs(a - b)                   
    # 차이를 구하는것 : 양수. b값이 더 크면 음수가 되므로 차이를 나타낸다 할 수 없음
    # 내장함수 abs()를 사용하거나
    # if 문을 사용하여 큰 값에서 작은값을 빼도록 계산
    # if a> b :
    #     result = a - b
    # else:
    # result = b - a
    return result
get_diff(4, 9)                       # -->> 이부분은 필요없음. 오류는 안나지만 딱히 쓸 필요 없고, 내가 알아보기 위해서 써보는것.
print(get_diff(4, 9))
# 또는 result = get_diff(4,9)
# print(result)
# 라고 해도 결과 나옴.
print("\n")








##       <<      실      습      >>
## 문제4) 가장 큰 수를 만드는 함수
##       함수에 입력된 5개 정수(0~9, 중복가능)를 사용하여 만들수 있는 가장 큰 수를 반환하는 함수를 정의하기
##       함수 이름 : get_biggest
##       파라미터 : a,b,c,d,e
##       반환값 : result

print("def 연습문제 4")                  #   ++++++++++++++ 모르겠다
# def get_biggest(a,b,c,d,e):
#     result = 
#     return result
# get_biggest(a,b,c,d,e)
# print()
print("\n")

print("def 연습문제 4 - 해설") 
# 큰 수가 앞에 오도록 정렬하는 문제로 볼 수 있다.
def get_biggest(a,b,c,d,e):
    # result = 0 
    # a,b,c,d,e
    # if a > b:
    #     if a > c:
    #         if a > d:
    #             if a > e:
    #                 result += a * 10000
    #             else : 
    #                 result =+ e * 10000
    #         else :
    #     else:
    # else:
    # 이런식으로 길게 짤 수 있음.
    numbers = [a,b,c,d,e]
    numbers.sort()
    result = 0
    for i in range(len(numbers)):       # numbers의 길이 5, 고로 범위 0 ~ 4
        result += numbers[i] * (10 **i)
    return result


# 다른 방법 - 2
# def get_biggest(a,b,c,d,e):
#     numbers = [a,b,c,d,e,]
#     numbers.sort(reverse=True)
#     result = ""
#     for i in numbers:
#         result =+ str(i)
#     return int(result)
print("\n")








##       <<      실      습      >>
## 문제5) 별 찍기 2
##       정수를 함수에 입력하여 호출하면 해당 정수 줄의 별을 화면에 출력한다.
##       함수 이름 : print_stars2
##       파라미터 : 
##       반환값 : 
"""
출력 결과
   *
  **
 ***
****
"""
print("def 연습문제 5")                        #  +++++++++++++++++ 모름!! 
# def print_stars2(n):
#     for i in range(n):
#         for j in range(n):
#             print("*", end="")
print("\n")

print("def 연습문제 5 - 해설") 
def print_stars2(n):
    # 리턴 필요 없으므로 생략
    # 공백을 넣어 주어야 함.
    # 별이 공백없이 가장 많을때 : n개
    for i in range(1, n+1):                  # 범위 1 ~ n
        print(" " * (n-i) + "*"*i)           # 공백을 넣고 싶을때 꼭 따옴표 안에 공백 넣어주기. 그냥 ""로 쓰면 안됨!!
print_stars2(5)
print("\n")

