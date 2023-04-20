# 4월 19일 3
# 수업 3,4 --------------------------------------------------------------

#      ********** 리스트 자료형 굉장히 많이 씀 ************

# 리스트 자료형
# 리스트(list)                   -> 당연히 변수 이름으로 list를 쓰면 안됨!
# 여러개의 값을 변수 1개에 저장
# 데이터 크기 생각 안해도 알아서 파이썬이 잡아줌.
# [1,2,3,4,5,6,7,8,9,]          ->  리스트 만드는 방법은 [값,값,값, .... , 값]
# [1,1,1,1,1,]                  ->  가능
# ["hello","world","python"]    -> 문자열도 넣을 수 있음.
# ["hello",2,"world"]           -> 숫자 문자 섞을 수도 있음.
# [1,2,["Hello","world"]]       -> 리스트 안에 리스트를 또 넣을 수 있음
# []                            -> 아무 값도 안 넣어도 됨. 나중에 추가하는것도 가능.
# 리스트 안의 값을 원소(element) 라고 함.


#       <<  실      습  >>
print("리스트 실습1")
# li_1=[1,2,3]
# print(li_1[0])
# print(li_1[1])
# print(li_1[2])
# print(li_1[-1])
# print( li_1[0] + li_1[1] )
print("\n")
print("리스트 실습2")
# li_2=[1,2,3,[4,5,6]] # 원소는 4개. 1,2,3 과 리스트1개
# print(li_2[3][0])  # 리스트 안의 리스트 안 원소 다시 가져오는방법 -> 옆에 붙여서 적기
# 인덱스 3번째에 있는 리스트의 인덱스0번째 데이터를 가져와라
print("\n")


# 행렬을 컴퓨터에서 나타내는 방법
# 행렬 모르면 인공지능 못함.
# 리스트를 두번을 겹치면 2차원이 됨.
# 행렬을 만드는 방법
# [[1,2,3],
# [4,5,6],
# [7,8,9]]

# 슬라이싱
print("리스트 슬라이싱1")
# print(li_2[2:3])
# print(li_2[1:])
# print(li_2[:2])
# print(li_2[3][0:2])
# print(li_2[0:1]) # 1번
# print(li_2[0]) # 2번. 1번과 2번은 범위는 동일해보이지만 리스트로 출력되는것(슬라이싱)과 정수가 출력되는것(인덱싱)으로 출력 데이터가 다름.
# 슬라이싱은 범위를 잘라서 가져오기 때문임.
print("\n")
print("실습: 출력결과가 [2,3]이 되도록 만들기")
# 출력 결과가 [2,3]이 되도록 만드세요
# li_3=[1,2,3,4,5]
# print(li_3[1:3])
# print(len(li_3)) # 리스트는 길이 체크 가능
print("\n")


# 리스트의 데이터 수정하기 --------------------
print("리스트의 데이터 값 수정하기")
# li_3[0]=10
# print(li_3)
print("\n")

# 리스트에 데이터 추가하기
# .append(원소)
# 리스트의 마지막에 원소를 추가
print("리스트에 값 추가하기")
# li_4=[1,2,3]
# li_4.append(4)
# li_4.append("문자") # 문자도 추가 가능
# print(li_4)
print("\n")

# 리스트에 내가 원하는 위치에 데이터 추가하기
# .insert(원소, 인덱스)   ->   인덱스 위치에 원소 삽입
print("리스트에 원하는위치에 값 추가")
# li=[1,2,3,2]
# li.insert(1, 10)  #  -> 1번 인덱스 위치에 10을 삽입
# print(li) # [1,10,2,3]
print("\n")


# 리스트에서 값 제거하기 1

# .remove(값)
# 리스트에서 함수에 입력된 값과 같은 값을 찾아 삭제함
print("리스트에 값 제거하기1")
# li.remove(2)
# print(li) # [1,10,3]
# 같은 데이터가 여러개 있는 경우 제일 왼쪽(첫번째) 있는 데이터만 삭제되고 뒤에 데이터는 남아있음.
# li.remove(2)
# print(li) # [1,10,3,2]
# 리스트 안에 없는 데이터를 삭제하라고 명령 내릴경우 오류가 남.
#li.remove(100)
#print(li)   #-> 오류남.
print("\n")


# 리스트에서 값 제거하기 2

# pop(인덱스)
# 리스트의 인덱스 위치의 요소를 **꺼냄**
# 인덱스를 함수에 전달하지 않으면 제일 마지막 요소를 꺼낸다.
print("리스트에 값 제거하기2")
# li=[1,2,3,4]
# li.pop()
# print(li)
# li.pop(1)
# print(li)
print("\n")
# remove와는 조금 다름. 꺼낸 변수를 저장 할 수 있음.
print("리스트와 팝 함수")
# li=[1,2,3,4,5]
# li.pop()
# a=li.pop()
# print(li)
# print(a)
# li.pop(1)
# b=li.pop(1)
# print(li)
# print(b)
print("\n")


# .index(값)
# 리스트에서 값을 찾아 그 값의 인덱스를 돌려준다.
# 인덱스를 알아내는 함수
# li[2]  ---> 인덱싱(인덱스로 값에 접근)
# li.index(값)   ---> 인덱스 알아내기
print("리스트와 인덱스")
# li=[1,2,3]
# idx=li.index(2) # 답 : 1
# print(idx)
# 없는 값을 넣으면 에러남. 없어서.
print("\n")


# .sort()
# 리스트의 요소를 정렬한다.
print("리스트와 정렬")
# li=[5,3,1,4,2]
# li.sort()
# print(li)  # 답 : [1,2,3,4,5] (오름차순)
print("\n")
# li.sort(reverse=True)  # 역방향 정렬 (내림차순)


# .reverse()
# 리스트의 순서를 뒤집는 함수
# 정렬하는것이 아님. 걍 뒤집어서 내놓는거.
print("리스트와 리버스")
# li=[5,1,3,4,2]
# li.reverse()
# print(li)
print("\n")


# .count(값)
# 리스트 안에 해당 값이 몇 개 있는지 세어서 몇개 있는지 개수를 알려준다.
print("리스트와 리버스")
# li=[1,2,3,2]
# li.count(2)
# cnt=li.count(2)
# print(cnt)    # 답 :2
print("\n")
# 리스트에 없는 데이터를 넣으면 답이 0 으로 나옴 ( 같은게 없다는 뜻)


# 리스트의 연산자
# + 연산자 : 리스트를 연결한다
print("리스트와 연산자")
li_1=[1,2,3]
li_2=[4,5,6]
print(li_1+li_2)  # 답 : [1,2,3,4,5,6]

# .extend(리스트) = + 연산자와 같은 기능
li_1.extend(li_2)
print(li_1)

# * 연산자 : 리스트를 곱한 수만큼 반복한다
li=[1,2,3]
print(li*3) # 답 : [1,2,3,1,2,3,1,2,3]
print("\n")

