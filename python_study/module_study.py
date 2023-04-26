# 4월 26일 5 -------------------------------------------------------------------------



# 모듈 :
# 함수, 변수, 클래스 등을 모아놓은 파이썬 파일
# 다른 파이썬 프로그램에서 불러와서 사용


# import 명령어로 불러옴 -
## 1. 첫번쨰 방법
"""
import 모듈이름(파이썬 파일 이름)
"""
print("모듈 - 예시1 ")
# import my_module
# my_module.add(1,2)
# my_module.sub(1,2)
print("\n")


## 2. 두번째 방법
"""
from 모듈이름 import 모듈함수
from 모듈이름 import 모듈함수1, 모듈함수2
from 모듈이름 import *(=전부가져온다)
"""
print("모듈 - 예시2 ")
# from my_module import add,sub
# add(1,2)                       # 함수 이름만 쓰고 호출하면 됨.
# sub(1,2)
print("\n")

# from my_module import *
# add(1,2)                       # 이것도 함수 이름만 쓰고 호출하면 됨.
# sub(1,2)
print("\n")



# 모듈 이해하기 연습 :
print("모듈 이해하기 - 연습")
import my_module
print("\n")










# 4월 26일 6-1 -------------------------------------------------------------------------


print("모듈 이해하기2")

from my_calculator import MyCalculator

# my_calculator = MyCalculator()
# my_calculator.div(10,2)
print("\n")





# 모듈의 오류 고치기 - 상속을 사용해 보기
# my_calculator = MyCalculator()
# my_calculator.div(10,0)                --->>> 0으로 나누면 오류남. 코드가 더이상 실행 안됨. 고로 0이 안들어가게 하면 됨. 어떻게??


print("모듈 이해하기3 - 상속 써보기")

class ZeroCalculator(MyCalculator):
    def div(self, n1,n2):                  # n1는 0 이어도 괜찮음. n2는 0이 오면 안됌.
        if n2 == 0:
            print("0으로 나눌 수 없습니다")    
        else:
            print(f"{n1} / {n2} = {n1 / n2}")

zero_calculator = ZeroCalculator()
zero_calculator.div(10,0)                  # 오류는 나나(0으로 못나누는데 나누라고 명령 내려서) 뒤의 코드가 실행되고 끝남. 에러를 잡아내는게 중요.

print("\n")




# 모듈의 오류 고치기 - 예외처리
# 예외처리
