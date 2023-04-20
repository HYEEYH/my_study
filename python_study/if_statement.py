# 4월 18일 3

# 수업4 --------------------------------------

# 조건문(if)

# 구조
#                        """if 조건:
# (탭한번, 스페이스네번 띄어쓰기) 실행하려는 코드"""
#  띄어쓰기 있음(->띄어쓰기 중요) 들여쓰기로 코드블럭을 구분.
# ex)))
# if 조건
#   실행하려는 코드
#   코드2줄
#   코드3줄
# 코드4줄
# )))
# 코트 ~3줄 까지는 조건문에 들어감. 코드4부터는 다른 코드 ~3까지를 코드블럭이라고 함.


# bool 타입
# True(참), False(거짓) -> 첫글자 대문자 반드시!
# bool 함수는 조건함수에 자주 쓰이는 코드


#  if문은 조건이 True(참)일때만 안쪽 코드블럭을 실행

# else
# if문과 짝궁처럼 따라다님. 단독으로는 사용 불가
# ex) if 조건:
#       조건일 참일때 실행하려는 코드
#     else:
#       아닐때 실행하려는 코드
# )))
# else는 조건이 False(거짓)일때 안쪽 코드 블럭을 실행

# elif 
# 조건이 하나 더 있을때
# ex)))
# if 조건1:
#   조건1이 True 일 때 실행
# elif 조건2:
#   조건1은 False, 조건2는 True일때 실행
# else:
#   조건1 False, 조건2 False일때 실행
# )))



#    <<<       실      습       >>>

# True 코드 작성
# number1=10
# number2=5
# if number1 > number2:
#     print(number1>number2)
#     print("number1이 더 크다")

# False 코드 작성 + else 코드 사용
number1=6
number2=7
if number1 > number2:
    print(number1>number2)
    print("number1이 더 크다")
else:
    print(number1>number2)
    print("number2가 더 크다")

# elif 코드 작성
# 등호 두개를 써서 같다는걸 표현 (등호 한개는 할당하는 연산자)
number1=6
number2=6
if number1 > number2:
    print(number1>number2)
    print("number1이 더 크다")
elif number1==number2:  # (주의) 맨 마지막에 ':' 이라고 적어줘야 제대로 작동한다!  ---> 틀렸던 부분임!
    print(number1==number2)
    print("같다")
else:
    print(number1>number2)
    print("number2가 더 크다")


# 비교 연산자
# a>b   : a가 b 보다 크다
# a>=b  : a가 b 보다 크거나 같다 ('=' 부등호가 앞에 오면 안됨)
# a<b   : a가 b보다 작다.
# a<=b  : a가 b보다 작거나 같다
# a==b  : a와 b가 같다
# a!=b  : a와 b가 같지 않다

#       <<<     실      습      >>>
print(2>3) # False
print(2>=3) # False
print(2<3) # True
print(2<=3) # True
print(2==3) # False
print(2!=3) # True

# 숫자가 아닌 알파벳으로 비교를 할떈 사전 기준으로 정해짐
# 사전에 먼저 오는 알파벳이 더 작다(뒤로 갈수록 커짐)
# a와 b를 비교하면 a가 더 작다 - 앞에 오는 수가 더 작다. (a < b < c < d < e < ..... < z)
# 대문자와 소문자의 경우 - 대문자가 앞에 오기 때문에 대문자가 더 작다.
#       <<<     실      습      >>>
print("CAT"<"DOG") # True
print("COW">"CAT") # True
print("DOG"=="dog") # False 대소문자 철저히 구분함.
print("DOG">"dog") # False 
# 문자열 비교는 자주 쓰지 않으나 ==은 많이 씀(ex.로그인 아이디가 같은지 구분할떄 등)


# 논리 연산자
# and  -> 주로 a and b 형태로 씀. *둘 다 참* 일때만 참 아니면 거짓
# or   -> 주로 a or b 형태로 사용. 둘 중 하나라도 참이면 참. 둘 다 거짓일 경우에만 거짓.
# not : 참이면 거짓으로 바꾸고, 거짓이면 참으로 바꾸고
#       <<<     실      습      >>>
print("and 연산")
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False
print("or 연산")
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False
print("not 연산")
print(not True) # False
print(not False) # True

# 실사용시 : 비교 연산자와 함께 사용
#       <<<     실      습      >>>
print("비교연산자와 논리연산자 사용")
# age=17
# if age>=20
#     print("성인입니다") # False라서 실행 안됨
# money=10000
# if money>=10000:
#     print("부자입니다")

# age=17
# money=10000
# if age>=20 and money >=10000:
#     print("성인이고 부자입니다") # 거짓 and 참 -> 결과 거짓. 고로 실행 안됨.
# if money>=10000:
#     print("부자입니다")

# age=17
# money=10000
# if age>=20 and money >=10000:
#     print("성인이고 부자입니다") # 거짓 and 참 -> 결과 거짓. 고로 실행 안됨.
# if age>=20 or money >=10000:
#     print("성인 또는 부자입니다") # 거짓 or 참 -> 결과 참. 고로 실행

# 문자타입과 숫자타입
# 문자열에 값이 있으면 참, 없으면 거짓 으로 취급
# 숫자 0 은 비어있는것으로 취급. 0이 아닌 숫자가 전부 참, 0은 거짓으로 취급
if "안녕":
    print("안녕하세요")
if 0:
    print(0) # 숫자0은 값이 없으므로 거짓. 고로 실행 안됨. 1은 참, 0은 거짓(이진법으로 표현하면 0은 00 -> 값이 없음)
    # 데이터 있는지 없는지 체크할때 쓰는 수식.


