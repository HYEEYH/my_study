# 4월 19일 1
# 수업 1 ------------------------------------------------------------
#       <<      실      습      >>

# <<문제 1>>
# eng변수, kor변수, math변수를 만들고 
# 각 변수는 과목의 시험 점수이다.
# 영어점수는 80점
# 국어 점수는 60점
# 수학 점수는 50점
# 세 과목의 평균을 내고
# 평균 점수에 따라 성적을 출력한다
# A : 91 ~ 100
# B : 81 ~ 90
# C : 71 ~ 80
# D : 61 ~ 70
# F : 60 이하

print("실습1")
eng = 80
kor = 60
math = 50
# 여기에 평균 낸 변수를 하나 더 만들면 좋다
# ex) avg = (eng + kor + math)/3
print("세 과목의 평균",(eng+kor+math)/3)
print("성적 결과")
if 100 >= (eng+kor+math)/3 >= 91:
    print("A")
elif 90 >= (eng+kor+math)/3 >= 81:
    print("B")
elif 80>= (eng+kor+math)/3 >= 71:
    print("C")
elif 70 >= (eng+kor+math)/3 >= 61: # 평균낸 변수를 사용해 수식의 중복을 최대한 줄이는 것이 좋다
    print("D")
else:
    print("F")
print("\n")

print("<<인풋 함수>>")
# input() : 인풋 함수
# (사용자로부터) 정보를 입력받는 함수
# 사용법 : 변수에 인풋 함수를 할당함
#      ->  user_input=input()
#       <<실        습>>
# # user_input=input()
# # print(user_input) # 사용자가 엔터를 누르기 전까지 적은 정보를 받음.

# 정수형 변환 함수
# int()
# integer(정수) 라는 영어에서 따옴
# 정수형, integer형, int형
# int(값) -> 이렇게 쓰면 정수형으로 바꿔줌(숫자모양이나 문자형인 데이터를 넣었을때. 아예 문자는 적용 X)



#       <<실습 코드에 인풋 함수 적용해보기>>
print("실습 코드에 인풋 함수 적용해보기")
eng = int(input("영어 점수:")) # 2. 이렇게 int를 앞에 붙여도 되고(숫자 문자열을 숫자형으로 바꾸기)

kor = input("국어 점수:")
kor = int(kor) # 3. 이렇게 따로 정의해줘도 됨. **** 인풋 먼저 정수변환 나중!***** 순서대로 코드 진행되니까!!

math = int(input("수학 점수:"))  # 1. 근데 이렇게만 하면 입력받은 정보는 문자열이 되어서 계산이 불가. *숫자형*으로 바꿔야함.
avg = (eng + kor + math)/3
print("세 과목의 평균",(eng+kor+math)/3)
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