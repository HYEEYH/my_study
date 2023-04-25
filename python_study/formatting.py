# 4월 25일 7 -------------------------------------------------------------------------

# 문자열 포매팅(formatting) : 
# 다양한 자료형들을 문자형으로 바꿀 수 있음.
# result = str(a) + "+" + str(b) + "=" + str(a+b) 를 다르게 표현하기 :
# (예시)
# result = "%d + %d + %d" % (3,2,5)
# print(result)
#
# (예시)
# a,b = 1,2
# result = "%d + %d + %d" % (a,b,a+b)
# print(result)




# 포맷 코드 :
# %s - 문자열 
# %d - 정수
# %f - 실수
# %o - 8진수
# %x - 16진수
# %% 글자 자체
# (예시)
# string1 = "Hello"
# int1 = 3
# float1 = 1.2345
# print("%s %d %f" % (string1, int1, float1))



# f-string :
# 파이썬 3.6 이후 버전부터 지원
string1 = "Hello"
int1 = 3
float1 = 1.2345
result = f"{string1}{int1}{float1}"
print(result)
# f"{}{}" 구조. 앞에 f 붙이면 알아서 문자열로 바꿔서 보여줌.