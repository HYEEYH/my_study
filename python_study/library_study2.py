# 4월 27일 1-2 -------------------------------------------------------------------------



# (cf)모듈을 모아둔거 : 패키지



# 표준 라이브러리
# 파이썬에서 지원하는 표준 라이브러리
# 파이썬을 설치할 떄 자동으로 함께 설치
# 따로 설치하지 않고 import 명령어로 불러옴











# 4월 27일 2 -------------------------------------------------------------------------



# 대표적 표준 라이브러리


# datetime 라이브러리 
# 날짜 관련 라이브러리

# datetime의 date객체 사용
print("datetime 라이브러리 예시1")
# import datetime
# day1 = datetime.date(2023,4,17)         # datetime에서 date를 사용하겠다
# day_end = datetime.date(2023,9,18)
# diff = day_end - day1
# print(diff.days)
print("\n")

print("datetime 라이브러리 예시2")
" 문) 2018년 8월 6일은 무슨요일일까? "
" * weekday()   -->>   0:월요일,  1:화요일,  ~~~ 6:일요일 "
# import datetime
# day = datetime.date(2018,8,6)
# print(day.weekday())                      # day의 weekday를 호출한다. 숫자로 표현함.
# weekdays = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]
# print(weekdays[day.weekday()])            # 리스트 인덱스 활용해 한글로 요일을 표시하기
print("\n")





# datetime의 포맷팅 코드
# 날짜랑 시간 표시하는 방법 :
# 년/월/일   
# 월/일/년
# 일/월/년
# 2023년 4월 27일
# 2020-04-27
# 23년 4월 27일

print("datetime 포매팅 예시")
# import datetime
# today = datetime.datetime.today()        # today()는 현재 시스템상의 시간을 가져옴.
# print(today)                             # strftime()를 이용하면 년 월 일이 한글로 써짐
# print(today.strftime("%Y년 %m월 %d일"))

print("\n")




# strftime()를 이용하면 년 월 일이 한글로 써짐
# "  %Y년  " - 년도 4자리 다 출력
# "  %y년  " - 년도 - 2자리 출력
# "  %m월  " - 월
# "  %d일  " - 일
# "  %H    " - 시간(24시간)
# "  %I    " - 시간(12시간)
# "  %M    " - 분                        # 소문자m : 월,   대문자M : 분
# "  %S    " - 초
# "  %A    " - 요일
print("strftime 포매팅 예시")
# print(today.strftime("%A"))
# print(today.strftime("%m"))
# print(today.strftime("%d"))
print("\n")




# time 라이브러리
# 시간 관련
# 만약 쓰는 방법을 모르겠다면 : python time document 라고 검색창에 검색하면 사용방법 알 수 있음.
print("time 포매팅 예시1")
# import time
# time_now = time.time()           # 현재 시간을 리턴
# print(time_now)                  # 컴퓨터에서 사용하는 시간이 나옴.
# print(time.strftime(" %H : %M : %S ", time.localtime(time_now)))   # 우리가 읽을 수 있는 시간으로 변환하는 방법
print("\n")



# time.sleep()
# 프로그램이 잠깐 멈췄다가 다시 진행됨.
# () 안에 초를 집어넣으면 됨 : 1을 집어넣으면 1초동안 멈췄다가 실행됨. 0.5(실수형)도 집어넣을 수 있음.
# 엄청 정확하게 1초 쉬는거 아님. 약1초임. 완벽하게 1초를 재서 진행하는게 아니다.
# 시간에 *굉장히* 민감한 프로그램을 만드는경우에는 사용하지 않는게 좋음.
# 크롤링(?) 할때 자주 쓰이기도 함 - 자료를 내려받는 코드를 짤 때 자료를 로딩하는 시간을 기다렸다가 진행시키기 위해
print("time 포매팅 예시2")
# import time
# print("before")
# time.sleep(1)
# print("after")
# for i in range(10):
#     print(i)
#     time.sleep(1)
print("\n")











# 4월 27일 3 -------------------------------------------------------------------------



# math
# 수학 관련 함수들
print("math 예시")
# import math
# result = math.ceil(1.1)              # ceil() : 올림 함수
# print(result)
# result1 = math.floor(1.9)            # floor() : 내림 함수
# print(result1)
# print(math.pi)                       # 파이 값도 가져올 수 있음
print("\n")



# random()
# 난수 관련 함수
# random.random() : 1.0 ~ 1.0 사이의 실수 중 난수 값 (아무거나 뱉음)
# random.randint(시작, 끝) : 시작 ~ 끝 사이의 정수 중 난수 값 (범위 내 수를 무작위로 뱉음. 시작과 끝 수 포함됨)
# random.choice(리스트) : 리스트의 요소 중 무작위로 하나를 리턴
# random.shuffle(리스트) : 
print("random 예시")
# import random

# "1"
# random_value = random.random()            # 실수 중 랜덤
# print(random_value)
# "2"
# random_value1 = random.randint(1,10)      # 정수 중 랜덤
# print(random_value1)
# "3"
# foods = ["서브웨이", "맥도날드", "짜장면", "국밥", "김치찌개"]
# random_value2 = random.choice(foods)      # 리스트 요소 중 랜덤
# print(random_value2)
# "4"
# li = [1,2,3,4,5]
# random.shuffle(li)                        # 데이터의 순서(위치)만 바꿔줌
# print(li)
# random.shuffle(li)
# print(li)
# random.shuffle(li)
# print(li)
print("\n")

print("random 로또 번호 얻어보기1")
import random
lotto_numbers = list(range(1,46))         # 리스트형으로 바꿔서 넣기
my_lotto = []
for i in range(6):
    random_value = random.choice(lotto_numbers)   # 초이스 함수는 중복해서 선택 할 수도 있음.
    if random_value not in my_lotto:              # 빈 리스트 만들어서 중복 선택 없애기
        my_lotto.append(random_value)
print(my_lotto)

print("random 로또 번호 얻어보기2")
lotto_numbers = list(range(1,46))
random.shuffle(lotto_numbers)
my_lotto1 = lotto_numbers[:6]
print(my_lotto)
print("\n")



# in 연산자
# a in b 형태로 쓰임
# a 가 b 에 포함되어 있으면 True
# a 가 b 에 포함되어 있지 않으면 False

# not in 연산자
# a not in b 형태로 쓰임
# a 가 b 에 포함되어 있지 않으면 True
# a 가 b 에 포함되어 있으면 False

print("in 연산자 예시")
# "1"
# li_1 = [1,2,3,4,5]
# a = 10
# for i in li_1:
#     if a == i:
#         print("이미 있음")        # ++++++ 리스트에 없어서 출력이 안된것. false값일경우 프린트하라는 명령이 없어서 종료된거임.
#     # else:                      # else 써주니까 출력 됨.
#     #     print("오류")

# "2"
# if a in li_1:
#     print("이미있음")
# # else:                          # else 써주니까 출력 됨.
# #     print("오류")

# "1 과 2는 같은 코드 다른 방식."
print("\n")











# 4월 27일 4 -------------------------------------------------------------------------



##       <<      실      습      >>
## 문제1)  색 이름과 음식 이름을 합치면 멋진 밴드 이름이 된다고 한다.
##        색 이름과밴드 이름을 무작위로 뽑아 밴드 이름을 추천하는 프로그램 만들기
"""
베이지 블랙 블루 회색 청색 레드 파란 핑크 그레이
쭈꾸미 오거트 오란다 와플 아이스티 떡볶이 커피
"""
print("문제1 - 연습 & 해설")

# import random       # 꼭 import 해줘야 뒤에 random 쓸때 오류가 안남

# li_co = ["베이지", "블랙", "블루", "회색", "청색", "레드", "파란", "핑크", "그레이"]
# li_fo = ["쭈꾸미", "요거트", "오란다", "와플", "아이스티", "떡볶이", "커피"]

# band_name = str(random.choice(li_co)) + str(random.choice(li_fo))
# print(band_name)

print("\n")











# 4월 27일 4~ 5~ 6 -------------------------------------------------------------------------

##       <<      실      습      >>
## 문제2) 숫자 야구 게임 만들기
##        숫자야구게임
##      1. 정답을 정한다. 정담은 4자리숫자(랜덤)
##      2. 게임 유저가 숫자를 입력한다
##      3. 정답과 비교해서 s/b/out 개수를 알려준다
##      4. 정답을 맞추거나, 종료를 입력하면 끝낸다
##      5. 답을 맞췄을때 '한번 더 하시겠습니까?' 를 넣어준다

print("문제2 - 연습&해설")
# import random

# # answer = random.randint(1000, 9999) 이렇게 해도 되나 중복숫자 있음
# "중복숫자 없이 가지고 오고 싶다면"
# numbers = list(range(10))
# random.shuffle(numbers)
# # answer = numbers[:4]                                             # 1. 근데 여기서 천의자리 숫자에 0이 오면 안됨
# answer = numbers[1:5] if numbers[0] == 0 else numbers[:4]          # 2. 삼항 연산자 사용. 제일앞에0 오면 1:5까지 가져오고, 아니면 앞에서4개 가져온다

# while True:
#     user_input = input("정답은?:")  # 문자열 데이터

#     if user_input == "종료":                  # --> 1@
#         print("종료합니다")
#         break
#     # 만약 문자열이 입력된다면 --> 다시 입력하게 한다 : 처음으로 간다 -> continue를 쓴다.
#     # if user_input == 숫자가 아니면 :
#     #     continue

#     # .isdisit() : 숫자로만 이루어진 문자열인지 확인한다.
#     # 숫자로만 이루어져있으면 True. 숫자 아니면 False

#     if not user_input.isdigit():              # --> 2@ 
#         print("숫자만 입력하세요")
#         continue

#     # 만약 4자리 숫자가 아니라면 다시 입력하게 한다
#     # -> 처음으로 간다 -> continue 사용
#     elif len(user_input) != 4:                # --> 3@
#         print("4자리 숫자만 입력하세요")
#         continue

#     # 만약 첫번째 자리 숫자가 0이 입력된다면
#     elif user_input[0] == "0":
#         print("첫번째 숫자로 0이 올 수 없습니다.")
#         continue

#     # 공백이 입력된다면 어떻게 할까?
#     # 예) "1234    " 이런식으로 숫자와 공백이 섞였을때. --> 2@부분에서 걸러짐.
#     # 예시에서 숫자+공백 부분에서 공백만 잘라서 숫자만 가지고 오고 싶을떄 -> user_input.strip()

#     # 중복 숫자를 확인할때 - 중복 있으면 안됨
#     duplicate = False                # 중복인지 아닌지 확인하기 위한 변수. 중복이 아니다 라는 의미
#     for i in range(3):               # 마지막 글자는 중복이건 아니건 어짜피 앞에서 체크하니까 할 필요 없음.
#         if user_input[i] in user_input[i+1:]:
#             duplicate = True         # 중복이 True라면 브레이크. 
#             break
#     if duplicate:                # 중복 아니라면 처음으로 돌아가서 계속함.
#         print("중복된 숫자가 없게 입력하세요")
#         continue
    


#     "<<나의 풀이>>"
#     # if len(user_input) > 4:
#     #     print("4자리 숫자를 입력해야합니다. 게임을 종료합니다")
#     #     break
#     # elif int(user_input) not in int:
#     #     print("숫자를 입력해야 합니다. 게임을 종료합니다")
#     #     break



#     strike = 0
#     ball = 0
#     out = 0

#     for i in range(4):
#         input_value = int(user_input[i])   # 입력 답의 i번째 숫자
#         if input_value not in answer:
#             out += 1
#         elif input_value == answer[i]:     # 입력 답의 i번째 숫자와 정답의 i번째 숫자가 같다.
#             strike =+ 1
#         else:
#             ball += 1

#     print(f"strike :{strike}, ball: {ball}, out:{out}")

#     if strike == 4 :
#         print("정답")
#         user_input = input("한번 더 하시겠습니까?[y/n]")
#         if user_input == "y":
#             numbers = list(range(10))
#             random.shuffle(numbers)
#             answer = numbers[1:5] if numbers[0] == 0 else numbers[:4]
#         else:
#             break
print("\n")

    


# 삼항 연산자 : 
# 구조 :
# 참일때값 if 조건 else 거짓일때값
print("삼항연산자 예시1")
# result = "참" if True else "거짓"
# result = "참" if False else "거짓"
# print(result)
print("\n")

print("삼항연산자 예시2") # n이 참이면 홀수, 거짓이면 짝수
# def odd_number(n):
#     return "홀수" if n % 2 == 1 else "짝수"
print("\n")










# 4월 27일 6 -------------------------------------------------------------------------


# os :
# OS 자원을 제어
# os.environ : 시스템의 환경 변수 값을 리턴한다.
# os.getcwd() : get current working directory. 현재 작업공간의 위치를 보여줌
# os.mkdir("디렉토리(=폴더이름)"") : 디렉토리(폴더)를 만든다
# os.rename("원래이름", "바꿀이름") : 파일의 이름을 바꾼다
# os.rmdir("디렉토리(=폴더이름)"") : 폴더를 지운다.   --->> (유의) 폴더가 비어있어야 함(아무것도 없어야 함)
# os.unlink("파일이름") : 파일을 지운다


print("os 예시1")
# import os
# print(os.environ)         # 함수가 아니고 변수라 괄호 없음.
# print(os.getcwd())
# os.mkdir("폴더1")
# os.rename("파일1", "파일2")
# os.rmdir("폴더1")
# os.unlink("파일2")
print("\n")









# 4월 27일 7 -------------------------------------------------------------------------

# os.path : 경로
# os.path.exists("경로") : 파일이 경로에 존재 하는지 않하는지 판별. 파일있으면 True, 없으면 False
# os.path.join("경로","경로","경로"): 경로를 합쳐서 1개의 경로로 만들어준다


print("os.path 예시2")
# import os
# if os.path.exists("없는파일"):
#     f = open("없는파일", "r")    # 이렇게만 하면 오류남
# else:
#     print("파일이 없습니다.")
# "또는"
# if not os.path.exists("없는파일"):
#     f = open("없는파일", "w")    
#     f.close
# else:
#     f = open("없는파일", "r")
print("\n")

print("os.path.join 예시3")
# import os
# cwd = os.getcwd()
# my_folder = "python_study"
# file_name = "test_file.txt"
# file_path = os.path.join(cwd, my_folder, file_name)
# with open(file_path, "w", encoding="utf-8") as f:
#     f.write("테스트파일을 작성합니다.")
print("\n")







# 외부 라이브러리


# 파이썬 표준 라이브러리가 아닌 라이브러리
# pip를 사용해 설치한다
# pip : package installer for python
# 파이썬 모듈, 패키지 설치하는 도구
# PyPI(Python Package Index) 파이썬 소프트웨어 저장공간에서 다운로드 할 수 있음.
# PyPI에 있는 파이썬 패키지를 설치해준다

# 패키지 설치
#  -->> pip install 패키지이름  : 명령어 입력시 패키지 설치해줌. 제일 최신 버전이 설치됨.

# 패키지 특정버전으로 설치
#  -->> pip install 패키지이름==1.0.5  :  이런식으로 버전을 명시해서 설치 할 수 있다.

# 패키지 삭제
#  -->> pip uninstall 패키지이름  : 명령어 입력시 패키지 삭제해줌.

# 패키지 최신버전으로 업그레이드
#  -->> pip install --upgrade 패키지이름

# 설치된 패키지 리스트 확인
# pip list
# 터미널에 치면 됨.
# 메뉴 - 터미널 - 뉴 터미널 열어서 거기다가 적어서 확인 할 수 있음

# pip freeze  -->> 나중에 뭔지 한번 찾아보기
# 패키지 어떤거 설치해놨는지 메모해놓는 명령어. 나중에 어떤버전 깔아놨는지 다시 찾아보기 위해 쓰임.


print("외부 라이브러리 예시1")
# import numpy, pandas, matplotlib, scikit-learn, keras, tensortflow, opencv.......   # 안깔려서 오류남


print("\n")









