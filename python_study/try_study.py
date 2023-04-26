# 4월 26일 6-2 -------------------------------------------------------------------------



# 예외처리 : 
# 오류의 발생을 잡아내서 처리하는 것
# 에러발생 시 프로그램을 중단하고 에러메세지를 보여준다.
# try 블록에는 오류가 발생할 수 있는 코드를 넣고
# except 블록에는 오류가 발생했을 때 수행할 코드를 넣는다.
# 오류가 발생하지 않으면 except 블록의 코드는 실행되지 않는다.
# 예외 처리 구문 형태 :
"""
try:
    오류발생 할 수 있는 함수
except:
    오류가 발생했을 때 수행할 코드     -->> 에러발생 없으면 실행되지 않는 코드
"""



## (예시1)
# print("에러 수정 - (예시1)")
# li = [1,2,3,4,5]
# li = [100]



## (예시3)
# print("에러 수정 - (예시3)")
# f = open("없는파일", "r")



## (예시2)
# print("에러 수정 - (예시2)")
# try:
#     100/0
# except ZeroDivisionError as e:
#     print("에러 발생")

# print("에러 발생 후")



## (예시4)
# print("에러 수정 - (예시4)")
# try:
#     100/0
# except Exception as e:          # 예외객체를 잡아서 에러메세지 출력. (e는 오류 객체. 오류가 들어있음. 프린트 시키면 오류 메세지 출력)
#     print(e)

# print("에러 발생 후")



## (예시5)
# print("에러 수정 - (예시5)")
# try:
#     100/0
# except ZeroDivisionError as e:           
#     print(e, "0으로 나눌 수 없습니다")

# print("에러 발생 후")



## (예시6)
print("에러 수정 - (예시6)")
# try:
#     [1,2,3,4,5][100]
# except ZeroDivisionError as e:                # 이 오류는 0으로 나눴을떄 나오는 오류만 잡아내는 코드. 고로 오류남.
#     print(e, "0으로 나눌 수 없습니다.")        # 여러개 에러를 처리할 수 있도록 다 써주던지, 에러 범용(Exception) 써주던지 해야함.
# except IndexError as e:
#     print(e, "인덱싱 할 수 없습니다.") 
# print("에러 발생 후")
print("\n")










# 4월 26일 7 -------------------------------------------------------------------------


# finally :
# 마지막으로 수행할 코드를 의미.
# 예외 발생 여부와 상관없이 항상 수행되는 코드

print("finally - 예시1")
# try:
#     f = open("없는파일", "r")
# except:
#     print("에러 발생")
# finally :
#     f.close()
print("\n")


# else :
# 오류가 발생하지 않으면 실행되는 코드

print("else - 예시1")
# try:
#     age = int(input("나이:"))
# except:
#     print("입력이 잘못되었습니다")
#     print("숫자를 입력해주세요")
# else:
#     if age >= 20:
#         print("성인입니다")
#     else:
#         print("미성년자입니다")
print("\n")




print("오류 만들어내기")
# 이거 구현 아직 안됐다고 알려주는 함수
# class Bird:
#     def fly(self):
#         raise NotImplementedError        # 함수를 호출하면 구현되지 않았다는 에러를 발생시킴. 일부러 발생시키는것.

# my_bird = Bird()
# my_bird.fly()           # --->>> 호출하면 아직 구현되지 않았다는 에러 메세지가 뜨게 됨.

print("\n")







##       <<      실      습      >>
## 문제4)  my_calculator 모듈의 MyCalculator 클래스를 상속받아 MaxCalculator 클래스를 정의하기
##          add, sub, mul, div 메소드를 사용하여 더하기,빼기,곱하기,나누기를 할 수 있다.
##          0으로 나눴을 때 에러가 발생하지 않도록 처리
##          입력되는 정수가 1개라도 100 보다 크면 계산하지 않고 100 이하의 값을 입력하도록 출력한다.
##          계산 결과가 100보다 크면 계산하지 않고 100 이하의결과가 나오는 값을 입력하도록 안내메세지를 출력한다
##          max_limit_calculator.py 파일에 작성하기

print("MaxCalculator 클래스를 정의 - 연습")

from my_calculator import MyCalculator

n1 = int(input("정수 1:"))
n2 = int(input("정수 2:"))

class MaxCalculator(MyCalculator):
    def add(self, n1, n2):
        print(f"{n1} + {n2} = {n1 + n2}")
    def sub(self, n1, n2):
        print(f"{n1} - {n2} = {n1 - n2}")
    def mul(self, n1, n2):
        print(f"{n1} * {n2} = {n1 * n2}")   
    def div(self, n1, n2):
        print(f"{n1} / {n2} = {n1 / n2}")

    try:
        n1 == '0'
    except ZeroDivisionError as e:           
        print(e, "0으로 나눌 수 없습니다")

    try:
        n1 or n2 >= 100
    except:
        print("100 이하의 값을 입력하세요")
    finally :
        pass

# -------------->>> 여기까지 하다가 끝남.

