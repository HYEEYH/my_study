# 4월 19일 6
# 수업 7 --------------------------------------------------------------
#       <<      실      습      >>
print("실습하기1")
"""

print("\n")
li_1=["Hello", "World", "Python"]
# li_1의 원소를 사용하여
# Hello World Python 이라고 출력하세요

print(li_1[0]+li_1[1]+li_1[2])         # -> 내가 쓴 답  
print(li_1[0],li_1[1],li_1[2])         # -> 답          1.

# 다른방법 ----> join(리스트) 사용하기  : 리스트의 문자열을 합친다
# " ".join(li_1)         : 문자열을 합치는다 ""안의 글자를 구분자로 하여 합친다. 이 경우엔 스페이스바(공백)
print(" ".join(li_1))                  #  ->  답         2.
print(li_1[0]+" "+li_1[1]+" "+li_1[2]) #  ->  답         3.
print("\n")


# li_1 의 원소를 사용하여
# Help 라고 출력하세요             ------>   의도는 글자를 가져와서 출력하라.
li_1=["Hello", "World", "Python"]
# li_1=[["H","e","l","l","o"], ["W","o","r","l","d"], ["P","y","t","h","o","n"]]
# print(li_1[0][0]+li_1[0][1]+li_1[0][2]+li_1[2][0])                               #  ----> 내가 쓴 답
print(li_1[0][0:3] + li_1[2][0])                                                 #  ----> 답 : 슬라이싱을 이용


li_2=[1,2,3]
# li_1과 li_2를 사용하여
#["Hello","World","Python",1,2,3] 을 출력하세요
print(li_1+li_2)
# 다른방법
# li_1.extend(li_2)
# print(li_1)
print("\n")


# li_1과 li_2를 사용하여
# ["Hello", 1, "World", 2, "Python", 3] 을 출력하세요    +++++++++++ 답에 정확히 일치하지 않음! 
        # 출제 의도 : insert 사용하라
print(li_1[0],li_2[0],li_1[1],li_2[1],li_1[2],li_2[2])
# 답
#li_1.insert(1, li_2[0])
#li_1.insert(3, li_2[1])
#li_1.insert(5, li_2[2]) 또는 li_1.append(li_2[2])
print("\n")
"""


#       <<      실      습      >>
print("\n")
print("실습하기2")
"""

scores = [] # 또는 scores=list()   ----> 안이 비어있는 리스트 만드는 두 가지 방법.
scores.append(int(input("영어 점수:")))
scores.append(int(input("국어 점수:")))
scores.append(int(input("수학 점수:")))

avg = (scores[0] + scores[1] + scores[2])/3
# sum()                               -----------> sum() : 더하기 함수
# 리스트의 요소를 모두 더한다.
# 숫자끼리만 더해야 한다. 문자 껴있으면 오류남.
# avg=sum(scores)/3 해도 같은값

print("세 과목의 평균",(scores[0] + scores[1] + scores[2])/3)
print("성적 결과")
if 100 >= avg >= 91:
    print("A")
elif 90 >= avg >= 81:
    print("B")
elif 80>= avg >= 71:
    print("C")
elif 70 >= avg >= 61: 
    print("D")
else:
    print("F")
"""
print("\n")


#       <<      실      습      >>
print("실습하기 3")
# 나이와 가지고 있는 돈을 입력받는다
# 가지고 있는 돈으로 물건을 몇 개 살 수 있는지와 잔돈을 출력한다
# 물건의 가격은 500원이다
"""
price=500
print(input("나이:"))
print(float(input("가지고 있는 금액:"))%price)"""

# 답
age=input("나이:")
money=int(input("돈:"))
price=500
print(money//price)
print(money%price)
print("\n")



print("실습하기4")
# 나이와 가지고 있는 돈을 입력받는다
# 가지고 있는 돈으로 물건별로 각 각 몇 개 살 수 있는지와 잔돈을 출력한다
# 물건의 가격은 1번물건 1000원
# 2번 물건 50원, 3번 물건 120원
'''price1=1000
price2=50
price3=120
print(int(input("나이:")))
mny=float(input("가지고 있는 금액:"))
print("1번 물건")
print("개수", mny//price1)
print("잔돈", mny%price1)
print("2번 물건")
print("개수",mny//price2)
print("잔돈",mny%price2)
print("3번 물건")
print("개수",mny//price3)
print("잔돈",mny%price3)'''

# 답   ---> 의도 : 리스트 사용해보기
age=input("나이:")
money=int(input("돈:"))
prices=[1000,50,120]
print(money//prices[0], money%prices[0])
print(money//prices[1], money%prices[1])
print(money//prices[2], money%prices[2])
