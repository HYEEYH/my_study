# 4월 20일 1
# 수업 1 --------------------------------------------------------------------------


# Whlie 반복문
# 동일한 동작을 여러번 반복해 동작하기 위해서 사용.
'''
while 조건:
    반복할 코드
'''
# (if 조건문과 유사한 형태)
# 조건이 참 인 경우에 코드를 계속 반복

# 만약 1~10까지 출력하려고 한다면:
# print(1) 
# print(2) 
# print(3) 
# print(4) 
# print(5) 
# print(6) 
# print(7) 
# print(8) 
# print(9) 
# print(10) 

# 이런식으로 계속 써야 하지만 whlie을 쓴다면 ->
print("실습하기1")
# n=1
# while n <=10:
#    print(n)
#    n+=1    #n=n+1 n에 1을 더해서 다시 n의 값으로 할당한다는 의미
print("\n")

# '+=' 연산자 : 대입연산자의 일종. 더하기 연산 후 할당
# n += 1은   ->   n = n+1 이라는 의미
# 산술 연산자 다 대입 가능
# -=    :  n -= 1    은    n= n-1 의 의미
# *=
# /=
# **=
# //=
# %=
# 연산자를 문자열에도 적용 가능
# s1="안녕"
# s1+="하세요"      # 이런 방식도 가능. 하세요랑 연결한 다음에 다시 할당해라 라는 의미
# s1 = s1 + "하세요"




#       <<      실      습      >>
# whlie 반복문을 활용하여
# 10부터 1까지 순서대로 출력하세요.
print("실습하기2")
# n1=10
# while n1 >=1:  # n1>0 이라고 써도 여기서는 같은 의미. 여기서는 정수형이라서 가능. (원래는 다름)
#     print(n1)
#     n1 = n1-1
print("\n")




#       <<      실      습      >>
# 커피 자판기 만들기 1
print("실습하기3")
# money = 10000
# price = 1000
# while money>=price:   # money-price >= 0 도 가능.
#     print("커피를 구매했습니다")
#     money -= price
print("\n")

# 커피 자판기 만들기
print("실습하기4")
# money1 = 10000
# price1 = 1000
# coffee = 5
# while money1 >= price1:   # money-price >= 0 도 가능./ 3.여기다가 커피 개수 조건 거는 방법도 있음.
#     print("커피를 구매했습니다")
#     money1 -= price1
#     coffee -= 1
#     print("남은 커피:", coffee) # 1.이대로 실행하면 남은 커피 개수가 마이너스까지 내려감.
#     if coffee==0:
#         break # 2. 반복문 안에서 조건을 따지지 않고 그 즉시 반복문을 빠져 나감. (앞에if있으니까 탭으로 한칸 들여쓰기)
print("\n")





# 수업 2 ---------------------------------------------------------------------------



# break
# 반복문을 즉시 종료한다.
# 특정 조건과 함께 사용 ( 보통은 if문)
#       <<      실      습      >>
# while 반복문을 활용하여
# 1부터 10까지 홀수만 출력한다.
print("실습하기5")
# a = 1
# while a <= 10:
#     if a % 2 == 1:
#         print(a)
#     a += 1
print("\n")



# continue
# 반복문의 제일 처음으로 돌아감.
#       <<      실      습      >>
# 1부터 10까지 홀수만 출력한다.       ++++++++++++++++++ 오류남. 왜일까
print("실습하기6")
# b = 0
# while b <= 9:
#     b += 1
#     if b % 2 == 0:
#         continue
#     print(b)
print("\n")




# 무한반복문  (= 무한루프)
# 조건식에 Ture를 입력해 항상 참이 되도록 하여 무한히 반복하게 한다.
# 대부분의 프로그램이 무한반복문 안에서 활동.
# 내가 끄기 버튼 누를 때까지 계속 동작함.
"""while True:   # 계산할 필요도 없이 무조건 참이 나옴. 계속반복됨. 전원 꺼질떄까지
    print("hi")"""

print("실습하기7")
# while True:
#     user_input = input("종료하려면 1을 입력 해 주세요:")
#     if user_input == "1":
#         break
print("\n")

# ### ctrl + c : 파이썬 안에서 실행을 강제종료 하는 단축키. ####
# 무한반복이 될때 눌러주면 멈춤.




#       <<      실      습      >>
# 무한 반복문으로 계산기 만들기
#+,-,*,/ 계산
# 2개의 수를 계산   ex) a + b
print("실습하기8")
# while True:
#     print("""
#     계산기
#     ==========
#     1. 더하기(+)
#     2. 빼기(-)
#     3. 곱하기(*)
#     4. 나누기(/)
#     """)
#     operator = input("계산을 선택하세요:")
#     if operator == "1":
#         print("1+2=", 1+2)
#     if operator == "2":
#         print("1-2=", 1-2)
#     if operator == "3":
#         print("1*2=", 1*2)
#     if operator == "4":
#         print("1/2=", 1/2)
print("\n")





# 수업 3 ---------------------------------------------------------------------------
#       <<      실      습      >>
# 무한 반복문으로 계산기 만들기
# 계산할 숫자도 입력받아 알맞은 계산을 하도록 수정해보기.
# 추가) q를 입력하면 종료되도록 변경하기.
print("실습하기9")
while True:
    print("""
    계산기
    ==========
    1. 더하기(+)
    2. 빼기(-)
    3. 곱하기(*)
    4. 나누기(/)
    """)
    operator = input("계산을 선택하세요:")
    num1 = int(input("숫자 입력1:"))
    num2 = int(input("숫자 입력2:"))
    if operator == "1":
        #print(str(num1) "+" str(num2), num1+num2) # +++++++++++++++++++ 오류남.
        # 수정 : 콤마 사이에 써 줘야 함
        print(num1, "+", num2, "=", num1+num2)

    if operator == "2":   # 1-4. 여기서부터 elif 사용해도 괜찮음.
        print(num1, "-", num2, "=", num1-num2)

    if operator == "3":
        print(num1, "*", num2, "=", num1*num2)

    if operator == "4":
        print(num1, "/", num2, "=", num1/num2)

    user_input = input("종료하려면 q을 입력 해 주세요:")
    if user_input == "q":
        break
print("\n")

# if 를 elif 로 바꾼다면 어떻게 동작되는가
# 기본 성질 : elif는 혼자 못쓰고 반드시 앞에 if 있어야 함
# elif = else 중에서 if 라는 뜻을 가짐.
# 만약 else를 계속 사용하려 한다면 :
'''
a=1
if a==2:
    print(2)
else:
    if a==3:
        print(3)
    else:
        print(1)
'''
# 1-1. 이런식으로 코드블럭이 계속 들어가게 되는것을 방지하기 위해 같은 뜻인 elif를 사용
# 1-2. 하나가 참일때 뒤에 값을 계산 또는 확인 할 필요가 없을경우 elif 쓰면 효율적.
# 1-3. 고로 실습9 에서 두번째 if 부터는 elif 사용해도 괜찮음.




# <<      실      습      >> ++++++++++++++++++++++++++++++++++++++++ 천천히 다시 보기
# 사용자가 가지고 있는 돈을 입력받는다
# 구매할 수 있는 커피의 개수와 잔돈 출력
# 구매할 수 있는 음료 개수와 잔돈 출력
# 구매할 수 있는 콜라 개수와 잔돈 출력
# 커피는 500원, 음료수 700원, 콜라는 930원
# 물품의 개수는 무한하다고 가정한다.
# while 반복문을 사용하여 작성한다.
print("실습하기10")
idx = 0
prices = [500,700,930]
money = int(input("돈:"))
while idx < len(prices):   #  ->   3. 하고싶은 만큼만 반복하게 하는 조건이 필요.
    # 1. while idx <=2  라고 쓸 수도 있음.
    # 2. while idx < 3
    # 4. 원소의 개수 체크 하는 함수를 사용해서 조건에 넣으면 매번 코드를 수정해야하는 수고를 줄일 수 있음.
    price = prices[idx] # 프라이스리스트 인덱싱함. 첫번째는 0이니까 0번에 있는 500을 할당. 프라이스는 0번째인 500이 됨.
    print(money // price)
    print(money % price)
    idx =+ 1
    break
print("\n")





# 수업 4 ---------------------------------------------------------------------------
# <<      실      습      >>
# while 반복문을 사용해서
# score 리스트에 시험 점수 5개를 정수형으로 입력받기.
print("실습하기11")
#### 나의 답. 와 모르겠네
# scores=[]
# score=int(input("시험 점수를 입력하세요:"))
# while len(scores) <= 5:
#     print(scores)
#     scores = score.append(int(input("시험 점수를 입력하세요:")))
#### 답
"""
scores=[]
n=0
while n < 5 :
    score = int(input("시험점수 :"))
    scores.append(score)
    n+=1
print(scores)    # 들여쓰기 잘 구분해야 함 탭 한번하면 리스트가 반복될때마다 출력, 탭 안하면 맨 마지막에 한번.
"""
print("\n")



# <<      실      습      >>
# while 반복문을 사용해서
# 구구단 2단을 출력하기.
print("실습하기12")

n=2
n1=1

while n1 <= 9 :
    print(n,"*",n1,"=", n*n1)
    n1+=1

print("\n")

