# 4월 26일 1 -------------------------------------------------------------------------





# 객체지향(oop, object oriented programming)
# : 객체와 객체 사이의 상호작용으로 프로그램을 구성하는 프로그래밍 패러다임

# 객체지향의 특징
# 1. 추상화 : 공통된 속성이나 기능을 도출  ->  구현하려고 하는 프로그래밍에서 주요한 특징만 남기는것. 
# 2. 캡슐화 : 데이터의 구조와 연산을 결합(하나에 한꺼번에 합친다는 느낌)
# 3. 상속 : 상위 개념의 특징이 하위 개념에 전달된다 (자동차 - (분화) - 트럭, 승용차, ....)
# 4. 다형성 : 유사 객체의 사용성을 그대로 유지. 사용성 극대화 
#           (상속과 연결)(공통 특징은 유지(자동차)- 세부적으로 다른 특징들을 추가(트럭칸 추가 등), 변경등 가능한...)

# 객체는 추상화와 캡슐화의 결과
# 객채는 데이터 필드와 메소드를 가진다

# 클래스는 객체를 정의한 것(객체의 설계도 (예시)붕어빵 틀: 클래스/ 객체 : 붕어빵)
# 데이터 필드(멤버 변수, 속성,... 등으로 부름) : 객체가 가지고 있는 변수
# 메소드 : 객체가 가지고 있는 함수

# 클래스 형식 :
"""
class 클래스 이름:
    클래스 멤버 변수
    메소드
"""

# 클래스 변수 이름 규칙 :  -->> 지켜줘야 함.
# 1. 영어, 숫자, 언더스코어(_) 가능
# 2. 제일 앞에 숫자 안됨
# 3. 키워드 사용 불가

# 클래스 이름 짓는 컨벤션(관용적으로 쓰이는 이름 규칙) :
# 1. 첫글자 대문자
# 2. 언더바(_) 안쓰기
# 3. 단어 구분될 때 대문자

# 클래스 이름 규칙 예시 :
print("클래스 이름 규칙 예시")
# class Car:
#     def move(self):         # Car 라고 하는 클래스를 통해서만 쓸 수 있는 함수가 됨. 코드블럭바깥에서 호출 불가(->일반함수와의 차이O)
#         print("move")       # 이렇게 클래스 안에 있는 함수를 -->> '메소드' 라고 함.

# class SportsCar:            # -->> 두글자 이상 결합 단어 : 첫글자 대문자, 띄어쓰기 안함, 언더바로 구분 안하고 대문자로 단어 구분
#     def move(self):
#         print("move")

# my_car = Car()              # -->> 호출하기. Car 클래스로 정의된 객체를 하나 만들고 마이 카 변수의 값으로 집어넣은것.
# my_car.move()               # 호출하면 출력됨. my_car 는 Car 클래스의 '인스턴스,객체,변수' 라고 표현하기도 함.

print("\n")

# 인스턴스 :
# 클래스를 통해 생성된 객체
# my_car.move() 에서 '.'이 뜻하는 것 : 객체 멤버 접근 연산자 (Car 안에 있는 함수를 쓰기 위해 접근한다 라는 개념)
#                                   앞에있는거 .(의) 뒤에있는거 실행해라











# 4월 26일 2 -------------------------------------------------------------------------


# 인스턴스 :
# 클래스를 통해 생성된 객체
# my_car.move() 에서 '.'이 뜻하는 것 : 객체 멤버 접근 연산자 (Car 안에 있는 함수를 쓰기 위해 접근한다 라는 개념)
# (예시)
# li= [1,2,3,4,5]
# li.append(6)   -  li 안에 있는 함수append를 사용하기위해 .을 써서 접근한다


# Python 에서는 모든게 객체다.


# 내장함수 type() :
# 데이터의 자료형을 반환하는 함수
# 리스트도 리스트 클래스의 객체다. 리스트는 파이썬 안에 이미 내장되어있던 함수
# 파이썬 안에서는 모든게 객체로 취급되어 돌아감. (정수형객체 실수형객체 리스트객체 ....함수도 객체로 취급)
print("내장함수 type() 예시")
# li= [1,2,3,4,5]
# # li.append(6)
# print(type(li))

# # print(type(n))
# print(type("Hello"))
print("\n")




# str(문자열) 메소드
# 문자열을 수정하게 되면 -> 수정한다 느낌이 아니라 새로 만들어낸다 느낌.
# upper() : 모두 대문자로 변경하는 함수
# lower() : 모두 소문자로 변경하는 함수
# strip() : 문자열 양쪽 끝의 특정 문자를 제거(보통 공백 제거할때 많이 씀)
# lstrip(), rstrip() : 왼쪽 끝 특정 문자 제거, 오른쪽 끝 특정 문자 제거 하는 함수.
# split() : 구분자로 분할하여 리스트로 반환하는 함수
# replace(바꾸고싶은글자, 바뀔글자) : 문자열의 특정 부분을 대체하는 함수


print("클래스 수업 - 문자열 함수 간단 예시")
# s = "Hello"
# s.upper()
# print(s.upper())
# print(s.lower())

# # strip() : 문자열 양쪽 끝의 특정 문자를 제거(보통 공백 제거할때 많이 씀)
# s1 = "    Hello    "
# print("1")
# print(s1.strip())

# # lstrip(), rstrip() : 왼쪽 끝 특정 문자 제거, 오른쪽 끝 특정 문자 제거 하는 함수.
# print("2")
# print(s1.lstrip())
# print("3")
# print(s1.rstrip())
print("\n")

# split() : 구분자로 분할하여 리스트로 반환하는 함수
# s2 = "Hello,World,Python"
# print(s2.split(','))

# # replace(바꾸고싶은글자, 바뀔글자) : 문자열의 특정 부분을 대체하는 함수
# print(s2.replace(',', ' '))
# print(s2)                    #  -->> 원본은 그대로고 새로운 객체를 만들어낸거.
#                              # 파이썬에서 문자열은 수정 불가한 객체임. 그래서 새로 만들어낸거
#                              # 변수 이름 그대로 쓰고싶으면 재할당 하면 됨. ex) s2 = s2.replace(',', ' ')


# Hello -> hello 로 바꾸고싶다면 : 
# s3 = "Hello"
# s3[0] = "h"
# print(s3)        # -->> 이렇게 쓴다면 오류남. 문자형 데이터는 수정이 불가한 데이터니까
# # s3 = lower()
# # s4 = s3replace("H","h")    # -->> 이렇게 해야 오류 안남.











# 4월 26일 3 -------------------------------------------------------------------------


# self 매개변수 :
# 모든 메소드의 첫번째 매개변수
# 메소드의 정의에는 사용되지만, 호출에는 사용되지 않음 ->
# 객체 자신을 참조하여 클래스에 정의된 멤버에 접근할 때 사용 
# 함수정의시 첫번째 매개변수에 필수로 self라 들어가야한다.

print("클래스 - self 매개변수 예시")

# class Person:
#     def say(self):
#         self.name = '사람1'     # 1. 멤버 변수. 클래스 안에서 자유롭게 사용 가능 (:객체 자신을 참조. 클래스에 정의된 멤버에 접근)
#         print("Hello")
#     def move(self):
#         pass
#     def eat(self, food):        # food 라는 매개변수 추가 시에도 맨 처음 self 무조건 먼저 넣어줘야 함.
#         self.sleep()            # 2. 이렇게 호출도 가능.
#         print(f"{self.name}이 {food}을 먹었습니다")
#         pass
#     def sleep(self):
#         print(f"{self.name}이 잠을 잤습니다")
#         pass
    
# person1 = Person()
# person1.say()                    # -->> 호출할떄는 self 안씀.
# person1.eat("밥")                # -->> 호출할때는 food만 호출.

print("\n")


# initializer :
# 초기자(초기 자)
# initialize 초기화가 일어날때 어떤 동작을 할건지 정해놓는것
# initialize 초기화 : (시작) 한다는 의미로 쓰임. (= '만든다' 라는 느낌과 유사. 값을 가지게 만든다.)
# 변수 객체가 만들어질때 (인스턴스가 생성될 때 ) initialize 된다.
# 초기값을 넣을때 주로 사용.


print("클래스 - initializer 예시")

# class Person:
#     # 1. def __init__(self, # name, age, gender, phone):             # initializer 구조.
#     # 1.     print("initialize")

#     def __init__(self, name, age, gender, phone):             # 4.
#         self.name = name       # 6. 이렇게 정의 해줘야 함.
#         self.age = age
#         self.gender = gender
#         self.phone = phone
#         print("initialize")
    
#     def say_name(self):
#         print(self.name)       # 5. 그냥 불러오면 오류남. name이 코드 밖에 있음. 고로 위에서 정의해줘야 함.



# print("before")         # 2. 인스턴스 생성 전
# person2 = Person("이름", 20, "남자", "010-1234-5678")    # 3. 원하는 정보 넣어주고 실행하면 에러남. 정보를 넣어줄꺼라 클래스에 정의 안함
# print("after")          # 2. 인스턴스 생성 후
# person2.say_name()      # 7.

print("\n")




##       <<      실      습      >>
## 문제1) person 클래스에 introduce 메소드를 추가
##       이름, 나이, 성별을 print 하는 메소드

print("클래스 연습 - 문1 ")

# class Person:
#     def __init__(self, name, age, gender, phone):
print("\n")


print("클래스 연습 - 문1 - 해설")

# class Person:
#     def __init__(self, name, age, gender, phone):             
#         self.name = name       
#         self.age = age
#         self.gender = gender
#         self.phone = phone
#         print("initialize")
    
#     def say_name(self):
#         print(self.name)
    
#     def introduce(self):
#         print(f"안녕하세요. 저는 {self.name}입니다")
#         print(f"나이는 {self.age}, 성별은 {self.gender}입니다.")
#         print(self.name, self.age, self.phone)

# person2 = Person("홍길동", 20, "남자", "010-1234-5678")
# person2.introduce()
print("\n")











# 4월 26일 4 -------------------------------------------------------------------------


# 상속 inheritance

print("클래스 - 상속 예시1")
# class Animal:   # 상위 클래스
#     def __init__(self, name):
#         self.name = name               # self.name과 name은 서로 다른 객체. 근데 값이 똑같음.
#         print(f"{self.name}이 생성되었습니다")

#     def say(self):
#         print("")

# class Dog(Animal):                     # ()안에 상속받을 클래스를 넣어준다. 상속받아 만들겠다
#     def say(self):                     # 메소드 재 정의 / method overriding(덮어쓰기): 부모클래스의정의가 없어지고 새로 정의한 메소드 호출함
#         print("멍멍")

# my_dog = Dog("백구")
# my_dog.say()


# class Cat(Animal):
#     def say(self):
#         print("야옹")

# my_cat = Cat("나비")
# my_cat.say()

print("\n")





##       <<      실      습      >>
## 문제2)  이름, 나이, 학교, 학년을 변수로 저장하는 메소드를 만들기

print("클래스 연습 - 문제2")

class Student:
    def __init__(self, name, age, school, grade):
        # 이름, 나이, 학교, 학년을 변수로 저장하는 메소드를 만들기
        self.name = name
        self.age = age
        self.school = school
        self.grade = grade
    
    def introduce(self):
        # 이름, 나이, 학교, 학년을 print하는 메소드를 정의하기
        print(f"안녕하세요. 저는 {self.name}입니다")
        print(f"저는 {self.age}살 이고, {self.school} 다니는 {self.grade}학년 입니다")

stu1 = Student("홍길동", 20, "서울대학교", 1)
stu2 = Student("손흥민", 21, "서울대학교", 2)
stu3 = Student("류현진", 22, "서울대학교", 3)
stu_li = [stu1, stu2, stu3]

for stu in stu_li:               # 리스트 만들어서 for문으로 반복
    stu.introduce()

print("\n")











# 4월 26일 5 -------------------------------------------------------------------------
##       <<      실      습      >>
## 문제3)  MyCalculator 클래스로 만들기
##          add, sub, mul, div 메소드

print("클래스 연습 - 문제3 + 해설 ")

class MyCalculator():
    def __init__(self):
        pass
    def add(self, n1, n2):
        print(f"{n1} + {n2} = {n1 + n2}")
        pass
    def sub(self, n1, n2):
        print(f"{n1} - {n2} = {n1 - n2}")
        pass
    def mul(self, n1, n2):
        print(f"{n1} * {n2} = {n1 * n2}")
        pass
    def div(self, n1, n2):
        print(f"{n1} / {n2} = {n1 / n2}")
        pass

my_calculator = MyCalculator()

while True:
    print(""""
    계산기
    1: +
    2: -
    3: *
    4: /
    q: 종료
    """)
    operator = input()
    if operator == 'q':
        print("종료합니다")
        break
    n1 = int(input("정수 1:"))
    n2 = int(input("정수 2:"))

    if operator == "1":
        my_calculator.add(n1, n2)
    elif operator == "2":
        my_calculator.sub(n1, n2)
    elif operator == "3":
        my_calculator.mul(n1, n2)
    elif operator == "4":
        my_calculator.div(n1, n2)
    else:
        print("잘못입력했습니다")

print("\n")






#  모듈




