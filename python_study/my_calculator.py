# 4월 25일 7 -------------------------------------------------------------------------


##       <<      실      습      >>
## 연습1) 계산기 만들기
##      기능: 두 정수의 사칙연산(+,-,*,/)
##      add(), sub(), mul(), div() 함수 정의
##      input() 함수를 활용하여 정수2개, 사칙연산 선택을 입력받은 후 계산 결과를 print한다.
##      계산식과 결과를
##      calculator_result.txt 파일에 기록한다.
##      사용자가 q를 입력하면 종료한다.

# print("연습1")

# # def add(a,b):
# #     return a+b
# # def sub(a,b):
# #     return a-b
# # def mul(a,b):
# #     return a*b
# # def div(a,b):
# #     return a/b

# # while True:
# #     print("""
# #     계산기
# #     1: +
# #     2: -
# #     3: *
# #     4: /
# #     q: 종료
# #     """)
# #     operator = input("원하는 식의 번호를 입력하세요:")
# #     if operator == 'q':
# #         break
# #     a = int(input("정수1 :"))
# #     b = int(input("정수2 :"))
# # # 함수는 호출 되기 전에 정의되어 있어야 한다.
# # # 고로 while 문 위에다가 정의해야함.
# #     if operator == "1":
# #         add(a,b)
# #         print(add(a,b))
# #     if operator == "2":
# #         sub(a,b)
# #         print(sub(a,b))            # 여기까지 하다 끝남.
# #     if operator == "3":
# #         mul(a,b)
# #     if operator == "4":
# #         div(a,b)
# #     result = 
# #     print(result)
# print("\n")



# print("연습1 - 해설")
# def add(a,b):
#     result1 = str(a) + "+" + str(b) + "=" + str(a+b)
#     print(result1)
#     with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(result1)

# def sub(a,b):
#     result2 = str(a) + "-" + str(b) + "=" + str(a-b)
#     print(result2)
#     with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(result2)

# def mul(a,b):
#     result3 = str(a) + "*" + str(b) + "=" + str(a*b)
#     print(result3)
#     with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(result3)

# def div(a,b):
#     result4 = str(a) + "/" + str(b) + "=" + str(a/b)
#     print(result4)
#     with open("python_study/calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(result4)


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
#     if operator == "2":
#         sub(a,b)
#     if operator == "3":
#         mul(a,b)
#     if operator == "4":
#         div(a,b)















        # 4월 26일 5 -------------------------------------------------------------------------
##       <<      실      습      >>
## 문제3)  MyCalculator 클래스로 만들기
##          add, sub, mul, div 메소드

# print("클래스 연습 - 문제3 + 해설 ")


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

if __name__ == "__main__":  # 실행 코드부분만 if 안쪽으로 넣어주어야 잘 움직임. 클래스(정의한 부분)는 넣지 말기.

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


# print("\n")
