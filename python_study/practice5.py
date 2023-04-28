# 4월 28일 1 -------------------------------------------------------------------------


# 지금까지 배운 것을 바탕으로 코드 만들기 실습 해보기.


####       <<      실      습      >>

## 문제1) 거꾸로 배열해도 같은 단어 또는 문장이되는 회문(palindrome)인지 판별하는 함수를 정의하기
##      함수에 문자열을 입력받고 회문이면 True
##      아니면 False 를 반환하도록 정의하기
##      함수 이름 : is_palindrome
##      반환값 : True 또는 False

print("문제1 - 연습")  #++++++++ 오류남
# # 문자열을 입력받기
# input("문자를 입력하세요:")
# # 입력받은 문자를 리스트에 넣기
# li_a = input("문자를 입력하세요:")
# # 리스트 리버스 사용해서 문자 뒤집기
# li_b = li_a.reverse()
# # 뒤집은 리스트 와 그냥 리스트 비교해서 문자열이 회문인지 판별하기
# def is_palindrome():
#     if li_a == li_b:
#         print(True)
#     else:
#         print(False)
# li_a = is_palindrome()
print("\n")


print("문제1 - 연습 - 해설1")
# def is_palindrome(input_string):
#     # 기러기 -> 
#     # 소주 만병만 주소 -> 
#     input_string = input_string.replace(" ","")     # 문자열 중간 공백 제거. " "공백부분을 ""공백없는걸로 대체해서 만들기


#     length = len(input_string)
#     for i in range(length//2):                      # -> 몫 연산자를 사용하여 길이의 절반만 for문 돌리기 절반만 확인해서 나머지랑 확인하면 되니까
#         length - 1          
#         if input_string[i] != input_string[length - 1 - i]:
#         # input_string[i] : 앞에서 한글자씩 반복
#         # input_string[length - 1 - i] : 마지막인덱스 - i : 뒤에서 한글자씩 반복
#             return False
#     return True
print("\n")



print("문제1 - 연습 - 해설2")
# def is_palindrome(input_string):
#     # 기러기 -> 
#     # 소주 만병만 주소 -> 
#     input_string = input_string.replace(" ","")  # 공백 제거. " "공백부분을 ""공백없는걸로 대체해서 만들기
#     return input_string == input_string[::-1]    # 뒤집는 함수 사용

# result = is_palindrome("다시 합창합시다 ")
# print(result)

print("\n")

# <참고>
# list.reverse : 원본이 뒤집어짐
#   -> 문자열.reverse 는 못함. 문자열데이터는 수정 불가
# reversed(시퀀스형 데이터) : 원본데이터를 그대로 새로운걸 만들어서 뒤집어주는 함수. 리턴을 받아야 함.
#   -> 근데 리버스 된 데이터랑 원본이랑 데이터형이 달라서 비교 불가

print("\n")










# 4월 28일 2 -------------------------------------------------------------------------

####       <<      실      습      >>

## 문제2) 코딩테스트 문제 풀어보기
##        온라인 코딩 테스트 사이트 : 
# # 백준. 
# # 소프트웨어 익스퍼트 아카데미 - 강의도 있음.
# # 프로그래머스 : 오늘은 여기서 코딩테스트를 가져와서 해볼꺼임.

print("문제2 - 연습")

print("\n")

