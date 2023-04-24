# 4월 24일 1 -------------------------------------------------------------------------



# function 함수
# 함수의 구조 : 입력 -> 처리-> 출력
# input(입력)을 받아서 특정 작업을 수행하고 output(출력)을 반환한다.

# 내장함수 (built-in function)
#  -> 파이썬이 기본적으로 제공해주는 함수.
# print()
# len()
# zip()
# int() -> 내장함수 맞음.
# str()
# list()
# range()




# abs()
# absolute 의 약자
# 입력한 숫자형 데이터의 절대값을 반환한다.
print("abs함수 예제")
print(abs(100))     # 답: 100
print(abs(-100))    # 답 : 100
print(abs(3.15))    # 답 : 3.15
print(abs(-3.15))   # 답 : 3.15
print("\n")




# sum(리스트)
# 리스트 안의 숫자를 모두 더한다.
# 더한 값을 반환한다
print("sum함수 예제")
print(sum([1,2,3,4,5]))
print("\n")




# max(리스트)
# 리스트 안에서 최대값을 찾아 반환한다.
print("max함수 예제")
print(max([1,2,3,4,5]))
print("\n")




# min(리스트)
# 리스트에서 최소값을 찾아 반환한다.
print("min함수 예제")
print(min([1,2,3,4,5]))
print("\n")




# chr(),   # ord()     -> 보통 세트로 많이 쓰는 함수.
# chr()    :  정수 1개를 입력받고 해당하는 유니코드 문자를 반환한다.
# (유니코드 문자마다 정해진 정수가 있음)
print("chr함수 예제")
print(chr(65))     # 결과 : A 가 나옴.
print("\n")
# ord()    : 문자 1개를 입력받고 해당하는 정수를 반환한다.
print("ord함수 예제")
print(ord("A"))     # 결과 : 65 가 나옴.
print("\n")




# round(값)
# 반올림 함수. 쓰는 방법은 2가지가 있음
# 1. round(값)              -> = round(값, 소수자리수=0)
# 2. round(값, 소수 자릿수) -> 소수 자릿수까지 남기고 반올림해라
print("round함수 예제")
print(round(1.234))        # 답 : 1     ()
print(round(1.234, 2))     # 답 : 1.23 ( 소수 두번째자리 남기고 반올림)
print(round(1.369, 1))     # 답 : 1.4  ( 소수 첫번째자리 남기고 반올림)
print("\n")






# 4월 24일 2 -------------------------------------------------------------------------


# 함수 정의(define).
# 함수를 정의하는 방법 ->
# 함수 이름
# 함수 입력값 (= parameter)
# 함수 결과값 (= return value)
# 을 정해주면 됨.
# 구조 :

"""
def 함수이름(함수입력값):
    함수 기능 코드
    return 함수 결과값
"""

# def는 함수를 정의하는 명령어
# 함수 이름도 변수 이름처럼 규칙을 지켜서 지어야한다.
# 1. 영어, 숫자, _만 사용
# 2. 숫자로 시작하면 안됨
# 3. 띄어쓰기 하면 안됨
# 4. 키워드 사용하면 안됨
# 5. 기존에 이미 정의된 함수 이름도 피하는 것이 좋음.
# -> print라고 함수 이름을 정의해서 사용할경우 파이썬 규칙 상 정의내린(def) 용법으로 먼저 사용.
# -> 오류 날 확률 높아짐.
print("def 예제1")
# def print_names():    # () 안이 비어있으므로 입력값이 없는 함수가 됨.
#     print("손흥민")
#     print("황희찬")
#     print("김민재")
#     print("이강인")     # 이 함수는 아웃풋이 없는 함수임. 
# print_names()          # 이 함수는 함수 안에 리턴 키워드가 없음. 이 함수로부터 나오는 값이 없음. 출력(수행)만 하고 종료
print("\n")




print("def 예제2")   # +++++++++++++++++++++++ 처음에 실행 안됨 -> 스펠링이랑 () 잘 입력해라....!!
# def get_name():
#     return "황혜리"   # 리턴 있음. 함수가 뱉는 값이 있다. 수행을 하고 값을 뱉어내고 종료.

# def print_my_name():
#     print(get_name())
# print_my_name()

# a= print_names   # 리턴이 없음
# b= get_name()  # 리턴이 있음

# print(a)     # None 나옴.
# print(b)
print("\n")




# parameter
# *****함수에 입력하는 값*******
# 매개변수, argument 혼용




print("def 예제3 - 리턴값이 있느냐 없느냐") # ++++++++++++++++++++++++++++ 리턴부터 이해가 안가....
# def add( a, b ):    # a,b(괄호 안의 내용들)는 함수의 매개변수, parameterm, argument 라고도 함
#     return a + b

# def print_add( a, b):
#     print(a + b)           # -> 이거 리턴 없음. 호출하면 None 나옴.

# # add()             # -> 그냥 호출만 하면 오류남. 왜? a,b값을 입력 안함.
# add(1,2)            # -> 이렇게 해야 오류 없이 호출됨.
# result = add(1,2)  
# print(result)       # 여기는 함수에 리턴값이 있어서 값이 출력됨.

# result = print_add(1,2)
# print(result)       # none이 나옴. 왜? print_add 함수에 리턴값이 없음. 
print("\n")





# 4월 24일 3 -------------------------------------------------------------------------
# 수업 2 def 함수 예제 3과 연결
print("def 예제4")
# print_add("안녕", "하세요")         # 슷자, 문자 둘 다 + 연산자 사용 가능하므로 실행 가능. 
# # # print_add("안녕", 1)           # 이건 에러 발생. 문자 + 숫자는 더할 수 없음.
# print_add("하세요", "안녕")         # 하세요 안녕 으로 출력됨. -->> ***위치(순서)***에 따라 전달받으므로 주의하기!
# print_add( b = "하세요", a = "안녕")         # 위치와 상관없이 매개변수 지정 가능
print("\n")


print("def 예제5-1")
# def swap_number(a, b):
#     temp = a           # temp 는 '임시' 라는 뜻. 임시로 변수 하나 만들어서 a 값 저장 했다가 b 에 넣는것.
#     a = b
#     b = temp
#     print(a, b)
# swap_number(1,2)
print("\n")


print("def 예제5-2")
# def swap_number(a, b):
#     temp = a                # temp 는 '임시' 라는 뜻. 임시로 변수 하나 만들어서 a 값 저장 했다가 b 에 넣는것.
#     a = b                   # 7. 지역변수 라고도 함. (코드블럭 안에서만 사용되는 변수)
#     b = temp
#     print(a, b)
#     # # 9. return a, b             : 라고 고치면 실행됨.

# a = 1                        # 8. 전역변수 라고도 함. (코드 전역에서 사용되는 변수)
# b = 2
# print("함수 호출 전", a,b)
# swap_number(1,2)             #  1. 함수 안에서는 서로 위치가 바뀜.   -->>   5. 함수 안 a,b 변수가 출력됨.
# # # 10. a, b = swap_number(1,2)    : 라고 고치면 실행됨.      
# print("함수 호출 후",a,b)     #  2. 근데 출력하면 그대로임. 왜?   -->>    4. 바깥 a,b 변수가 출력된 것.
# # # 3. 함수 안에서 쓰는 a,b와 함수 바깥에서 쓰는 a,b가 달라서 나오는 결과. 이름만 같은 변수들.
# # # 6. 블럭으로 구분되는 함수들은 다 이 규칙을 적용받음.
print("\n")




##       <<      실      습      >>
## 문)  다음 함수를 정의하세요
##      함수 이름 : mul
##      함수 입력값 : 정수 2개
##      함수 출력값 : 정수 2개의 곱

print("def 연습문제 1") #+++++++++++++++++++++++++++++++ 오.. 모르겠는데...
# def mul(a, b):
#     a = 1
#     b = 4
#     print(mul)
#     return a*b
print("\n")

print("def 연습문제 1 해설")
# def mul(n1, n2):
#     return n1*n2
# 여기서 프린트 하려면
# 1. print(mul(1,2))   # 또는 
# 2. result = mul(1,2)
#    print(result)
print("\n")




# # cf))) 팁 -> 
# # a = 1
# # b = 2
# # c = 3    #은 줄여서
# # a,b,c = 1,2,3  이라고 줄여서 쓸 수도 있음. 리스트도 됨. 튜플도 됨.
# # d,e,f = (4,5,6) 튜플의 d는 4, e는 5,..... 가능
# # g,h,i = [7,8,9]








# 4월 24일 4 -------------------------------------------------------------------------

# ****기본값 매개 변수****
# 함수에 기본값을 넣어 둘 수 있음
# default value parameter
# 함수 호출시에 n2에 입력된 값이 없으면 기본값 사용 한다는 뜻.

print("def 예제 6")
# def mul(n1, n2=1):       # 'n2=1'이런식으로 값을 지정해서 넣을 수 있음.
#     return n1*n2
# mul(1,2)
# mul(1)
print("\n")


print("def 예제 7-1")
# def test_func(x, test=[]):
#     test.append(x)
#     print(x, test)
# test_func(1)       # 답 : [1]
# test_func(2)       # 답 : [1,2]       # 리스트는 지역변수지만 전역변수처럼 사용됨.
print("\n")
# # ((결론)) : 기본값으로 리스트는 쓰면 안됨. 값이 누적되기때문에


print("def 예제 7-2")
# def test_func1(x, test = 5):
#     test = test
#     print(x, test)
# test_func1(1)       
# test_func1(2)
print("\n")


print("def 예제 7-3")    # 예제 7-1처럼 속이 비어있는 리스트처럼 사용하고 싶다면
# def test_func2(x, test = None):
#     if test == None:
#         test=[]
#     test.append(x)
#     print(x, test)
print("\n")



# 기본값 사용할 떄 지켜줘야 하는 규칙이 있음.
print("def 예제 8")
"""
def sub(n1, n2=0, n3):      # 이거 불가. 
    print(n1 - n2 - n3)
"""
# 기본값이 있는 매개 변수는 기본값이 없는 매개변수보다 뒤에 위치해야 함.
"""
def sub(n1, n3, n2=0):      # 이렇게 써야 함.
"""
print("\n")





# *args
# 예시) 1 ~ 10 까지 더한다    라고 하면,
# 수가 많아지면 코드를 적기 힘들어짐 -> *를 사용한 매개변수를 사용하면 됨.
# 입력값이 몇개가 될 지 모를때(안 정해졌을때) 사용하는 방법.
# add_many(1,2,3)  --->> 답 6
# add_many(1,2,3,4,5,6,7,8,9,10)  -->> 답 55

print("def 예제 9")
# def add_many(*args):
#     # 튜플처럼 사용 -> 인덱싱, 슬라이싱, for문 등 사용가능.
#     result = 0
#     for i in args:
#         result += i
#     return result
# result1 = add_many(1,2,3,4,5)
# print(result1)
# result2 = add_many(3,2,5,9,2)
# print(result2)
# result3 = add_many(1,2)
# print(result3)

# def calc_many(n1, *args):                    # ()괄호 안의 문자는 순서 바꿔서도 사용 가능. 일반 매개 변수와 같이 사용 가능.
#     result = n1
#     for i in args:
#         result += i
#     return n1
print("\n")





# 키워드 매개변수
# **kwargs -> keyword arpuments
# 딕셔너리로 사용
# 뒤에 들어오는(매개변수) 값이 유동적일때 많이 사용
# 매개변수 형태로 처리 안하고 함수 안으로 들여와서 처리.
# 잘 모르고 쓴다면 에러 날 확률 높음  -->>  사용을 많이 안하는 추세. 알고만 있자.
print("def 예제 10 - 키워드 매개변수")
# def print_kwargs(**kwargs):
#     print(kwargs)

# print_kwargs(a=1, b=2)   # 키워드를 명시해서 넣어줘야 함.
# print_kwargs(name='이름', age='나이')
print("\n")





# 함수의 반환
# return 반환값 --->>> 값을 반환함과 동시에 함수가 종료.
print("def 예제 11 함수의 반환 - 1")
# def test_func5():
#     print(1)
#     print(2)
#     return None                               # return 만나는 순간 함수 중료. 밑은 실행 안됨.
#     print(3)
#     print(4)
#     print(5)
print("\n")

# ***함수의 반환값은 무조건 1개이다.***
print("def 예제 11 함수의 반환 - 2") 
# def test_func6(a, b):
#     return a + b 
#     return a * b   # 여기는 실행 안됨.
print("\n")
#  -->>  return a + b, a*b                      # 이렇게 쉼표로 구분해서 한줄에 다 써야함. 튜플형태로 출력 
#  -->> 튜플형식으로 a=1, b=2일때 결과 : (3, 2) : 튜플형식으로 출력됨

# res_add, res_mul = test_func6(1,2)            # +++++++++++++++++++++++++++++++++++++ 아이참 뭔소리야...
# => 같음 : res_add, res_mul = (a+b, a*b)







# 4월 24일 5 -------------------------------------------------------------------------
## 오전시간 배운 내용 복습








# 4월 24일 6 -------------------------------------------------------------------------
##       <<      실      습      >>
## 문제) 홀수 판별 함수
##      정수 1개를 입력받고 홀수인지 판별하는 함수
##      함수 이름 : is_odd_number                   # (is.../has...로 시작)보통 이런 형태의 함수이름은 참/거짓 판단가능한것일때 많이 씀.
##      파라미터 : n
##      반환값 : 홀수면 True, 짝수면 False

print("def 연습문제 2")
# def is_odd_number(n):
#     if n % 2 == 0:
#         print(True)
#     else :
#         print(False)
#     return n
print("\n")

print("def 연습문제 2 - 해설1")
# def is_odd_number(n):
#     if n % 2 == 1:
#         return True
#     else:
#         return False
# is_odd_number(5)    # 함수 호출하기
print("\n")

print("def 연습문제 2 - 해설2")    # 해설1과 결과 같음.
# def is_odd_number(n):
#     if n % 2 == 1:
#         return True                  # 참일경우 리턴을 만나서 함수 종료. 
#     return False                     # 거짓일경우 if 문 바깥으로 나가서 리턴 만남.
print("\n")

print("def 연습문제 2 - 해설3")    # 해설1과 결과 같음.
# def is_odd_number(n):
#     return n % 2 == 1                # 조건 바로 계산해서 조건 채로 리턴. 조건이 참이면 참, 거짓이면 거짓이 나오니까.
print("\n")



##       <<      실      습      >>
## 문제) 테두리를 출력하는 함수
##      문자열을 입력받고 print 함수를 이용해 테두리와 함께 문자를 출력한다.
##      함수 이름 : get_bordered_str
##      파라미터 : message
##      반환값 : None                                         # 출력과 반환값 혼동하지 않기! 구분 잘하자!
##      print 예시  : 
"""
        *****  # * 표시는 입력된 문자열 길이만큼 출력.
        hello
        *****
"""
print("def 연습문제 3")
# def get_bordered_str(message):                    
#     print(len(get_bordered_str(message))*"*")
#     print(get_bordered_str(message))
#     print(len(get_bordered_str(message))*"*")
# get_bordered_str("hi")


# ## 오류가 났던 이유) print(len(get_bordered_str(message))*"*") : 이 위에서 함수를 정의하는 중임.
# ## 근데 코드블럭 안쪽에서 계속 정의중인 함수를 불러와서 실행을 반복하게 됨 --->>> 오류남.
print("\n")


print("def 연습문제 3 - 해설")
# def get_bordered_str(message):
#     n = len(message)
#     print("*" * n)
#     print(message)
#     print("*" * n)
# get_bordered_str("hi")
print("\n")


print("def 연습문제 4")
# 메세지에 숫자 12345 를 넣었을때 오류가 나는데 이걸 해결하기.
# def get_bordered_str(message):
#     n = len(message)
#     print("*" * n)
#     print(message)
#     print("*" * n)
# get_bordered_str("12345")        #  --->>> 이거 아냐~
print("\n")

print("def 연습문제 4 - 해설 ")
# def get_bordered_str(message):
#     message = str(message)     #  -->   # len 함수는 숫자에 못씀. 문자형, 리스트, 튜플 (시퀀스형 데이터에만) 사용가능 고로 문자형으로 바꿔줌
#     n = len(message)
#     print("*" * n)
#     print(message)
#     print("*" * n)
# get_bordered_str(12345)          
print("\n")







# 4월 24일 7 -------------------------------------------------------------------------
##       <<      실      습      >>
## 문제) 속도를 변환하는 함수
##      m/s 단위의 속도가 입력되면   ->   km/h 단위의 속도로 변환한다.
##      함수 이름 : convert_velocity
##      파라미터 : velocity
##      반환값 : km/h로 변환된 속도

print("def 연습문제 5")
# def convert_velocity(velocity):
#     return (velocity*3600)/1000

# convert_velocity(10)
print("\n")


print("def 연습문제 5 - 해설")
# 1초에 1미터 -> 1m/s
# 1m/s 로 한시간 동안 가면 몇m? : 1m/s * 3600초(1시간)
# 3600m/h
# 1km = 1000m. 3600/1000 -> 고로 1m/s = 3.6km/h
# 초속(변수) * 3600 / 1000 --> 시속
# 초속 * 3.6 = 시속

def convert_velocity(velocity):
    result = velocity * 3.6
    return result

print(convert_velocity(10))    # 프린트 함수 써줘야 출력된다
print("\n")






##       <<      실      습      >>
## 문제) 별 찍기 함수
##      정수를 함수에 입력하여 호출하면 해당 정수줄(n줄)의 별을 화면에 출력한다.   ++++++++++++ 모르겄다~~~~~
##      함수 이름 : print_stars
##      파라미터 : n
##      반환값 : None
"""
출력 결과 
n ->1
*

n ->2
*
**

n ->4
*
**
***
****
"""
print("def 연습문제 6 -  해설1")
def print_stars(n):
    for i in range(n):           # i = 0 ~ n-1 까지 들어감
        for j in range(i+1):     # j = 0 ~ i 까지 들어감
            print("*", end="")   # end="" : 원래 기본값으로 end값에 줄바꿈이 되어있어서 자동으로 줄바꿔 프린트 됨. ""는 비우라는 뜻. 줄바꿈안하고 거기서 끝내라는 뜻
        print()                  # 아무것도 출력 안하고 end의 기본값인 줄바꿈만 하라는 의미
print("\n")

print("def 연습문제 6 -  해설2")
def print_stars(n):
    i = 0
    while i < n:
        j = 0
        while j < i + 1:
            print("*", end="")
            j += 1
        print()
        i += 1
print("\n")