# 4월 27일 1-1 -------------------------------------------------------------------------


##       <<      실      습      >>
## 문제4)  my_calculator 모듈의 MyCalculator 클래스를 상속받아 MaxLimitCalculator 클래스를 정의하기
##          add, sub, mul, div 메소드를 사용하여 더하기,빼기,곱하기,나누기를 할 수 있다.
##          0으로 나눴을 때 에러가 발생하지 않도록 처리
##          입력되는 정수가 1개라도 100 보다 크면 계산하지 않고 100 이하의 값을 입력하도록 출력한다.
##          계산 결과가 100보다 크면 계산하지 않고 100 이하의결과가 나오는 값을 입력하도록 안내메세지를 출력한다
##          max_limit_calculator.py 파일에 작성하기


# print("MaxCalculator 클래스를 정의 - 연습 - 해설")

# import my_calculator 해도 ㅇㅋ
from my_calculator import MyCalculator

class MaxLimitCalculator(MyCalculator):
    def add(self, n1, n2):
        if n1 > 100:
            print("100보다 작은 수를 입력하세요")
        elif n2 > 100:
            print("100보다 작은 수를 입력하세요")
        else:
            result = n1 + n2
            if result > 100:
                print("계산 결과가 100보다 작아야 합니다")
            else:
                print(f"{n1} + {n2} = {n1 + n2}")

    def sub(self, n1, n2):
        if n1 > 100:
            print("100보다 작은 수를 입력하세요")
        elif n2 > 100:
            print("100보다 작은 수를 입력하세요")
        else:
            result = n1 - n2
            if result > 100:
                print("계산 결과가 100보다 작아야 합니다")
            else:
                print(f"{n1} - {n2} = {n1 - n2}")

    def mul(self, n1, n2):
        if n1 > 100:
            print("100보다 작은 수를 입력하세요")
        elif n2 > 100:
            print("100보다 작은 수를 입력하세요")
        else:
            result = n1 * n2
            if result > 100:
                print("계산 결과가 100보다 작아야 합니다")
            else:
                print(f"{n1} * {n2} = {n1 * n2}")   

    def div(self, n1, n2):
        if n1 > 100:
            print("100보다 작은 수를 입력하세요")
        elif n2 > 100:
            print("100보다 작은 수를 입력하세요")
        elif n2 == 0:
            print("0으로 나눌 수 없습니다") 
        else:
            result = n1 / n2
            if result > 100:
                print("계산 결과가 100보다 작아야 합니다")
            else:
                print(f"{n1} / {n2} = {n1 / n2}")

# 또는 0으로 나누지 말라는 메세지를 출력하고 싶을때
        # else:
        #     try:
        #         result = n1 / n2
        #     except ZeroDivisionError:
        #         print("0으로 나누지 마세요")
        #     if result > 100:
        #         print("계산 결과가 100보다 작아야 합니다")
        #     else:
        #         print(f"{n1} / {n2} = {n1 / n2}")






my_max_limit_calculator = MaxLimitCalculator()     # 이니셜라이저 호출하기. 변수에 객체를 집어넣어서 객체(MaxLimitCalculator())를 시작(새로 만든다)
my_max_limit_calculator.div(100,0)



# print("\n")


