# 4월 20일 1
# 수업 5 --------------------------------------------------------------------------



# for문 (for 반복문)
'''
for 변수 in iterable값:
    반복할 코드
'''
# iterable : 순회, 가능하다  -> 리스트 같은 것들. 인덱싱 슬라이싱 할 수 있는 것들. 숫자는X(값이하나임)

print("for문 예시1")
li_1=["one","two","three"]
for i in li_1:
    print(i)
print("\n")

# 첫번째 요소부터 마지막 요소까지 변수에 대입하면서 반복

print("for문 예시2")
s1="hello"
for i in s1:
    print(i)
print("\n")




#       <<      실      습      >>
print("실습하기 13")
numbers=[1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)
print("\n")

print("실습하기 14") # ++++++++++++++++++++++++++++++++++++ 이거 뭐 빠뜨린거같은데...
# 역순으로 정렬하고 싶으면 
numbers.reverse()
for number in numbers:
    print(number)       # number와 munbers 구분해야지! 리스트 안에서 넘버를 빼서 돌려야한다!
print("\n")




# range(반복을 원하는 횟수)
# 정수여야 함.
"""
1. range(끝 정수) : 0 ~ 끝정수-1
2. range(시작, 끝) : 시작 ~ 끝 정수-1
3. range(시작, 끝, 스탭) : 시작 ~ 끝-1 까지인데 스텝만큼 차이나게
"""
print("실습하기 15") # 1.
for i in range(10):
    print(i)
print("\n")

print("실습하기 16") # 2.
for i in range(1,11):  # 1~10까지
    print(i)
print("\n")

print("실습하기 17") # 3.
for i in range(1,21,2):
    print(i)
print("\n")




#       <<      실      습      >>
# 1. for 문을 사용하여 2부터 30까지 출력해보기
# 2. for 문을 사용하여 2부터 30까지 숫자 중 짝수만 출력해보기
# 3. for 문을 사용하여 10부터 1까지 출력해보기
print("실습하기 18") 
print("문1.") 
for i in range(2,31):
    print(i)
print("\n")

print("문2.")
for i in range(2,31,2):
    print(i)
print("\n")

# if 문을 쓴다고 가정하면
print("문2-1.")
for i in range(2,31):
   if i % 2 == 1:   # 홀수
       # continue      -> 여기서는 이거 쓸 수 있음. 근데 매번 되는거 아님 이거는 다시 처음부터 진행. ++++++++++++
       pass           #-> 아무것도 안하고 바깥으로 빠져나감. 뒤의 코드 진행. 아무것도 안하고 넘어갈때 씀.+++++++++
   else:   # 짝수
       print(i)
print("\n")

print("문2-2.")
for i in range(2,31):
    if i % 2 == 0:    # 짝수라는 뜻
        print(i)
print("\n")

print("문3.")  # ++++++++++++++++++++++++++++++++++++++++++++ 이거 모르겠다.
for i in range(10,0,-1):
    print(i)
print("\n")

print("문3-1.")
for i in reversed(range(1,11)):
    print(i)
print("\n")

print("문3-2.")
for i in range(1,11)[::-1]:        # 1. 슬라이싱 보통[:] 형태로 썼으나 ::로 :를 두개 쓰면 방향을 지정할 수 있음
    print(i)
print("\n")
# 2. [시작인덱스:끝인덱스:방향]  방향에  -1 쓰면 거꾸로 감.
#      생략시0   생략시0   -1     ->   -1만 썼으므로 거꾸로 슬라이싱함.





# 수업 5 --------------------------------------------------------------------------
#       <<      실      습      >>       ++++++++++++++++++++++++++++ 되게 헷갈려!! ++++++++++++++++++++++++++++++
# 커피 사기
print("실습하기 19")
"""
money = 10000
price = 1000
coffee = 5

print("답1.")
for i in range(coffee):  # 범위 : 0~4
    print("커피를 구매했습니다")
    money =- price   # money = money - price
    print("남은 커피:", coffee - 1 - i) # 4~0의 값이 나와야함. 처음 출력할떄 이미 커피를 팔았으니까.
print("\n")

print("답2.")
for i in range(1, coffee+1):  # 1 ~ 5
    print("남은 커피:", coffee-i) # 4 ~ 5
print("\n")

print("답3.")
for i in range(coffee):
    coffee -= 1
    print("남은 커피:", coffee) # 4 ~ 0 
"""
print("\n")





# 수업 6 --------------------------------------------------------------------------

#       <<      실      습      >>       
# for문에서 break 써보기

print("실습하기 20")

money = 2000
price = 1000
coffee = 5

for i in range(coffee):  # 범위 : 0~4
    print("커피를 구매했습니다")
    money -= price   # money = money - price     # ------>> 연산자 순서 조심!! +++++++++++++++++++++++++++++++++++++
    print("남은 커피:", coffee - 1 - i) # 4~0의 값이 나와야함. 처음 출력할떄 이미 커피를 팔았으니까.
    if money < price:
        break

print("\n")

print("실습하기 21")    # 횟수가 정해져 있을때에는 while 보다 for 쓰는게 편할 떄가 많다.
"""prices = [500, 700, 930]
money = int(input("돈:"))
for i in range(len(prices)):
    price = prices[i]
    print(money//price)
    print(money%price)"""
print("\n")

print("실습하기 22")      # *********** 제일 간단하게 사용하는 방법 ***********
"""prices = [500, 700, 930]
money = int(input("돈:"))
for price in prices:
    print(money//price)
    print(money%price)"""
print("\n")

print("실습하기 23") 
"""scores = []
for i in range(5):
    score = int(input("시험점수:"))
    scores.append(score)"""
print("\n")

print("실습하기 24") # 구구단 2단 만들기
for i in range(1,10):   # 1 ~ 9
    print("2*",i,"=", 2*i)
print("\n")



# 이중 for문
"""
for i in range()
   for j in range()
    print()
"""
print("실습하기 25") # 구구단 2 ~ 9단 까지 반복하게 만들기   ---->> 반복문 안에 반복문 넣기 ********중요함*******
"""for i in range(2,10):   # 2 ~ 9           큰 루프 안의
    print(i, "단")
    for j in range(1,10): # 1 ~ 9         작은 루프   -> 작은 루프 먼저 다 돌아가고 큰 루프 돌아감.
        print(i,"*",j,"=", i*j)
    print("------------------")"""

print("\n")