# 5월 1일

# 데이터
# 코렙 사용해보기
# 웨일온 사용해보기(화상회의프로그램)


print("연습1")
# a = [5,4,3,2,1,]
# b = a[:]
# print(id(a),id(b))
print("\n")

# 참고
# 튜플 만들떄 a = (3, )
# 처럼 빈 공간을 만드는 것을 가변공간이라고 해서 혹시 몰라 공간 남겨두는것.

# set연산자 주의사항(코렙)
# 3 and 4 : 4 가 나옴(둘 중 큰 수 나옴)
# 3(=0011) and 4(=0100): 논리연산자가 아님. -> 비트연산자 이기 때문에
# or 도 마찬가지(둘 중 작은 수 나옴


print("연습2")
# a = 5
# b = 7
# print(a==b)
# print(a or b)
# c = 5
# d = 3
# print(c==d)
print("\n")



## 문제1) b로 a를 나눈 나머지가 3 초과면 실패, 3이면 무승부, 3 미만이면 성공이 출력되도록 만들어보기
print("연습 문제 1")
# a = int(input("숫자1: "))
# b = int(input("숫자2: "))
# num = a // b

# if num > 3:
#     print("실패")
# elif num == 3:
#     print("무승부")
# else:
#     print("성공")
print("\n")


## 문제2) 태어난 연도를 계산하여 학교 종류를 맞추는 프로그램 당신이 태어난 연도를 입력하세요 2000 학생이 아닙니다

## 나이는 현재년도- 태어난년도+1
## 26세이하 20세이상이면 대학생
## 20세미만 17세 이상이면 고등학생
## 17세 미만 14세 이상이면 중학생
## 14세 미만 8세 이상이면 초등학생
## 그 외의 경우 학생이 아닙니다 출력

print("연습 문제 2")
print("\n")



## 문제 3) 숫자로 범위주기 5에서 0까지 카운트다운 세보기
print("연습 문제 3")
# for count in range(5,-1,-1):
#     print(count)
print("\n")
# 5,0,-1 이 아니라 5,-1,-1이라는거 조심하기!



## 문제 4) 1부터 10까지 더하기 (range함수 이용)
print("연습 문제 4")
# sum = 0
# for i in range(1,11):
#     sum = sum+i
# print(sum)
print("\n")


## 문제 5) 별 찍기 연습
## 1. 계단형
## 2-1 삼각형(왼쪽 아래가 직각인)
## 2-2 삼각형(오른쪽 아래가 직각인)
## 3-1 역삼각형(왼쪽 위가 직각인)
## 3-2 역삼각형(오른쪽 위가 직각인)
## 4. 피라미드

print("연습 문제 5")
# 1
# n = int(input("숫자입력:"))

# for i in range(n):
#   print(""*i, end = "")   # end 역할 : sep와 비슷한 기능(구분자 사용)
#   print("*"*n)

# # 2-1
# n = int(input("숫자를 입력하세요:"))

# for i in range (1, n+1):
#   print("*"*i)

# # 2-2
# n = int(input("숫자를 입력하세요:"))

# for i in range (1, n+1):
#   print(" "*(n-i), end="")
#   print("*"*i)

# # 3-1
# n = int(input("숫자를 입력하세요:"))

# for i in range(n):
#   print("*"*(n-i))

# # 3-2
# n = int(input("숫자를 입력하세요:"))

# for i in range(n):
#   print(" "*i, end="")
#   print("*"*(n-i))

# # 4
# n = int(input("숫자를 입력하세요:"))

# for i in range(n+1):
#   print(" "*(n-i), end="")
#   print("*"*(2*i-1))
print("\n")





## 문제 6) x = [3,6,9,20,-7,5]의 값의 모든 요소에 10을 곱한뒤 출력하기
### 문제 6-1) 심화) 출력과 리스트x의 값에도 모두 10을 곱하기
print("연습 문제 6")
print("\n")





## 문제 7) y = {"math":70, "science":80, "english":20}의 값의 모든 요소에 10을 더한 뒤 출력하세요
### 문제 7-1) 심화) 출력과 딕셔너리 y의 값에도 모두 10을 더해주세요
print("연습 문제 7")
print("\n")





## 문제 8) 숫자를 입력받고 입력받은 정수의 구구단을 출력하기
print("연습 문제 8")
print("\n")






## 문제 9) 1~100 임의의 숫자를 맞추기
print("연습 문제 9")
# import random

# true_value = random.randint(1,100)
# input_value = 99999  #(임의의 값 할당)

# n = int(input("숫자를 맞춰보세요(1~100):"))

# while true_value != input_value:
#     input_value = int(input())
#     if input_value > true_value:
#         print("숫자가 큽니다") # 사용자의 입력값이 true_value보다 클때
#     else:
#         print("숫자가 작습니다")
# print(f"정답입니다. 입력한 숫자는 {true_value}입니다")

print("\n")






## 문제 10) word = ["school", "game", "piano", "science", "hotel", "mountain"] 중 
##          글자수가 6글자 이상인 문자를 모아 새로운 리스트를 생성하기
print("연습 문제 10")

# word = ["school", "game", "piano", "science", "hotel", "mountain"] 
# a = list()

# for i in range(len(word)):
#   if len(word[i]) >= 6:
#     a.append(word[i])
# print(a)

print("\n")







## 문제 11) 1 - 100 까지의 숫자 중
## 3과 5의 공배수일경우 "3과 5의 공배수"
## 나머지 숫자 중 3의배수일 경우 "3의 배수"
## 나머지 숫자 중 5의 배수일 경우" 5의배수"
## 모두 해당되지 않을 경우 그냥 숫자를 출력하기.
print("연습 문제 11 풀어봄")

# n = int(input("숫자를입력: "))

# if n%3 == 0:
#     if n%5 == 0:
#         print("3과 5의 공배수")
#     print("3의 배수")
# elif n%5 == 0:
#     print("5의 배수")
# else:
#     print(n)


print("연습 문제 11 심화버전 해설")
# 정수를 입력했을때 1~ 입력받은정수 까지 모든 수의 3,5 배수를 판별하기

# b = int(input("정수를 입력하세요"))
# if b<=0:
#   print("음수는 정의하지 않음")
# else:
#   for a in range(1, b+1):
#     if a % 3 == 0 and a % 5 == 0:
#       print("3과 5의 공배수")
#     elif a%3 ==0:
#       print("3의 배수")
#     elif a%5 == 0:
#       print("5의 배수")
#     elif 1 <= a <= 100:
#       print(a)
#     else:
#       print("1과 100 사이의 숫자가 아닙니다")
print("\n")






## 문제 12) 사용자로부터 숫자를 계속 입력받다가 s or S를 입력하면 합계출력

print("연습 문제 12")
# c = 0
# d = 1

# while (d==1):
#     a = input()
#     if (a=="s" or a == "S"):
#         d=0
#     else:
#         a = int(a)
#         c +=a
# print(c)
print("\n")






## 문제 13) 사람 별 평균을 구하기
print("연습 문제 13")
kor_score = [39,69,20,100,80]
math_score = [32,59,85,30,90]
eng_score = [49,70,48,60,100]
midterm_score = [kor_score, math_score, eng_score]


student_score = [0,0,0,0,0]
i = 0
for subject in midterm_score:  # 과목 선택
    for score in subject:    # 과목선택 후
        student_score[i]+=score  # 각 학생마다 개별로 교과 점수를 저장
        # print(subject,score,'i:,i,student_score)   # kor->math->eng 
        i+=1   # 학생 index구분
    i=0
else:
    a,b,c,d,e = student_score  #학생별 점수를 unpacking
    student_average = [a/3, b/3, c/3, d/3, e/3]
    print(student_average)








# (참고)
# print({:.20f},format(1/3)) --> 20번째자리까지 계산하라는 의미.
# 보통 컴퓨터는 16번째 자리까지 계산하기때문에 16자리 이후로는 오류가 남.

