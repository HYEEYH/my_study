# 4월 25일 4 -------------------------------------------------------------------------




# 파일 입출력
# -> 파이썬에서 파일 생성, 수정



# open()
# 파이썬 내장 함수
# 파일을 열고, 파일 객체를 리턴한다.
# 사용방법 : 
# open("파일이름(=파일경로)", '파일 열기 모드')
# 실 사용 연습
print("파일 열기 사용 연습")
# f = open("C:/Users/405/my_study/python_study/새파일.txt", 'w')  # 이건 절대경로.
#     # 새파일.txt 라는 파일을 파이선_스터디 안에 만든거
# f.close()
#     # 오픈했다면 꼭 클로즈 해줘야 함.
print("\n")


# 파일의 경로 :
# 절대 경로 - C:/ 또는 D:/ 처럼 최상단 경로부터 나타낸 경로
# 상대 경로 - 현재 작업 위치부터 나타낸 경로

# 파일 열기 모드 :
# r - 읽기모드. 파일을 읽기만 할 때 사용 
# w - 쓰기모드. 파일에 내용을 쓸 때 사용
#     덮어쓰기된다. 실행 할 때마다 전에 쓴 내용 다 사라지고 새 내용이 들어감.
# a - 추가모드. 파일의 마지막에 새로운 내용을 추가할 때 사용


print("파일 열기 사용 연습 - 쓰기모드")
# f = open("python_study/새파일.txt", 'w', encoding="utf-8")       # 메모장은 한글이 유니코드로 나타나기때문에 유니코드 쓰라고 해야 제대로 출력
# for i in range(1, 11):
#     print(i, "번째 줄",)            # 출력함수 : 터미널 화면에 출력
#     f.write(str(i)+"번째 줄\n")     # 출력함수 : 파일 안에 데이터 출력               # ************* 또 이해 안되는 코드 구성이구만.
#     # 기본 - 줄바꿈 안됨. 줄바꿈 하고 싶으면 뒤에 \n을 써줘야 함.
# f.close()
print("\n")


print("파일 열기 사용 연습 - 추가모드")
# f = open("python_study/새파일.txt", 'a', encoding="utf-8")
# for i in range(11, 21):              # 범위 : 11 ~ 20
#     print(i, "번째 줄")
#     f.write(str(i)+"번째 줄\n")
# f.close()
print("\n")







# 4월 25일 5 -------------------------------------------------------------------------

print("파일 열기 사용 연습 - 읽기모드1")
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# line=f.readline()               # readline() 함수 사용
# print(line)                     # 첫번째쭐 읽어옴
# line=f.readline()               # 두번째 줄 읽어옴.
# print(line)
# f.close
print("\n")




# readline()  :
# 첫번째 줄 부터 1줄 읽어온다.
# 커서가 이동하는 것처럼 읽어옴




print("파일 열기 사용 연습 - 읽기모드2")
# 한줄씩이 아니라 모두 읽어오고 싶을 떄
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# while True:
#     line = f.readline()
#     if line == " ":
#         break
#     print(line)
# f.close  
print("\n")




# readlines() :              ---->>> readline 아님. 뒤에 s 붙어있음.
# 파일의 모든 줄을 읽어서 리스트로 반환



print("파일 열기 사용 연습 - 읽기모드3")
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# lines = f.readlines()
# for line in lines:      # -->> 이렇게 안쓰고 프린트만 하면 줄바꿈 없이 횡으로 쭉 가져옴. 줄바꿈 하고싶으면 한줄씩 꺼내서 프린트
#     print(line)
# f.close
print("\n")




# read() 함수 :
# 파일 내용 전체를 문자열로 리턴한다.




print("파일 열기 사용 연습 - 읽기모드4")
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# data = f.read()
# print(data)
# f.close()
print("\n")





# for문으로 읽는 방법:

# print("파일 열기 사용 연습 - 읽기모드5")
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# for line in f:
#     print(line)
# f.close
print("\n")




# 보통은 리드라인/ 리드라인즈 주로 사용함.



# with 문:
# open - close를 자동으로 해준다
print("파일 열기 사용 연습 - with")
# with open("python_study/새파일.txt", 'a', encoding="utf-8") as f:
#     f.write("end of file")              
    # 코드블럭 안쪽에서 실행하는 동안만 오픈하겠다
    # 코드블럭에서 나가는 순간 열었던 파일이 닫힘.
    # 따로 클로즈 해 줄 필요 없으나 꼭 탭 안에서만 써야 함.
    # a 모드로 작성해도 만약 파일이 없다면 새 파일을 만들어서 내용을 쓴다.
# #f.write     # --->> 여긴 오류남. 왜? 블록 밖이라 이미 파일 닫혔음.









# 4월 25일 6 -------------------------------------------------------------------------



# csv(comma separated values) :
# 콤마로 구분되는 값을 모아놓은 파일. 쉼표와 줄바꿈으로 표현해놓음.
# (예시)----------------------
#   이름,입실시간,퇴실시간,
#   권오천,9:20,18:10
#   김예진,09:21,18:11
# ---------------------------

print("파일 열기 사용 연습 - csv")
# with open("python_study/data.csv", "w", encoding="utf-8") as f:
#     f.write("날짜,날씨,기온\n")
#     f.write("20230424,맑음,10\n")
#     f.write("20230425,비,9\n")

# with open("python_study/data.csv", "r", encoding="utf-8") as f:
#     data = f.readlines()
#     print(data)

print("\n")





##       <<      실      습      >>
## 문제1) 계산 결과 저장 함수
##      정수 2개를 입력받고 두 수를 더한 결과를 add_result.txt 파일에 저장하는 함수를 정의하기
##      함수 이름 : add_write
##      파라미터 : 
##      반환값 :

print("파일 열기 사용 연습문제1")
# with open("python_study/add_result.txt", "w", encoding="utf-8") as f:
#     def add_write(a,b):
#         result = a + b
#         f.write(result)
#         print(result)
print("\n")

print("파일 열기 사용 연습문제1 - 해설")
# def add_write(a,b):
#     # a + b --> write에 쓰면 됨.
#     result = a + b
#     with open("add_result.txt", "w", encoding="utf-8") as f:      # 경로지정안했으니 현재 작업위치에 만들어짐.
#         f.write(str(result))                    # 그냥 쓰면 안되고 문자열로 바꿔서 써 줘야함.
# add_write(1,2)
print("\n")







##       <<      실      습      >>
## 문제2) 텍스트파일에 적힌 정수 2개를 읽어와서 더하는 함수를 정의하기.
##      텍스트 파일 이름 : add_number.txt
##      경로 : python_study/add_number.txt
##      정수 2개를 더한 결과를 print 하기. 
##      함수 이름 : read_add_print

print("파일 열기 사용 연습문제2")           # 아이고 다틀리네
# def read_add_print(a,b):
#     with open(add_result.txt", "w", encoding="utf-8)
print("\n")

print("파일 열기 사용 연습문제2 - 해설") 
# def read_add_print():
#     with open("python_study/add_number.txt", "r", encoding="utf-8") as f:
#         data = f.read()
#         a = int(data[0])            # 데이터를 읽어오면 다 문자열. 정수형으로 바꿔줘야 함.
#         b = int(data[2])            # 공백도 인덱스가 읽음.
#         print(a+b)
# read_add_print()
print("\n")










# 4월 25일 7 -------------------------------------------------------------------------


##       <<      실      습      >>
## 연습1) 계산기 만들기
##      기능: 두 정수의 사칙연산(+,-,*,/)
##      add(), sub(), mul(), div() 함수 정의
##      input() 함수를 활용하여 정수2개, 사칙연산 선택을 입력받은 후 계산 결과를 print한다.
##      계산식과 결과를
##      calculator_result.txt 파일에 기록한다.
##      사용자가 q를 입력하면 종료한다.

print("연습1")

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b

# while True:
#     print("""
#     계산기
#     1: +
#     2: -
#     3: *
#     4: /
#     q: 종료
#     """)
#     operator = input("원하는 식의 번호를 입력하세요:")
#     if operator == 'q':
#         break
#     a = int(input("정수1 :"))
#     b = int(input("정수2 :"))
# # 함수는 호출 되기 전에 정의되어 있어야 한다.
# # 고로 while 문 위에다가 정의해야함.
#     if operator == "1":
#         add(a,b)
#         print(add(a,b))
#     if operator == "2":
#         sub(a,b)
#         print(sub(a,b))            # 여기까지 하다 끝남.
#     if operator == "3":
#         mul(a,b)
#     if operator == "4":
#         div(a,b)
#     result = 
#     print(result)
print("\n")



print("연습1 - 해설")
def add(a,b):
    result1 = str(a) + "+" + str(b) + "=" + str(a+b)
    print(result1)
    with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
        f.write(result1)

def sub(a,b):
    result2 = str(a) + "-" + str(b) + "=" + str(a-b)
    print(result2)
    with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
        f.write(result2)

def mul(a,b):
    result3 = str(a) + "*" + str(b) + "=" + str(a*b)
    print(result3)
    with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
        f.write(result3)

def div(a,b):
    result4 = str(a) + "/" + str(b) + "=" + str(a/b)
    print(result4)
    with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
        f.write(result4)


while True:
    print("""
    계산기
    1: +
    2: -
    3: *
    4: /
    q: 종료
    """)
    operator = input("원하는 식의 번호를 입력하세요:")
    if operator == 'q':
        break
    a = int(input("정수1 :"))
    b = int(input("정수2 :"))
# 함수는 호출 되기 전에 정의되어 있어야 한다.
# 고로 while 문 위에다가 정의해야함.
    if operator == "1":
        add(a,b)
    if operator == "2":
        sub(a,b)
    if operator == "3":
        mul(a,b)
    if operator == "4":
        div(a,b)






# 문자열 포매팅(formatting) : 
# result = str(a) + "+" + str(b) + "=" + str(a+b)
# result = "%d + %d + %d" % 3,2,5