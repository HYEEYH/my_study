# 4월 18일 2

# 수업3 --------------------------------


# 변수
# 메모리의 데이터가 있는곳을 표시하는것 : 주소
# 변수 : 메모리에 어떤 값을 가리키는 이름 (주소로 가리키는건 너무 길고 복잡하므로 간단하게 표현한것)
# 변수 : 값이 있음. 변수 안의 데이터 정보가 중요
# = : 할당연산자. 
# ex) number = 10 에서 number 는 변수의 이름, 변수에 10이라는 값을 넣어 놓겠다는 의미 (number에 10을 할당)
# 변수를 그대로 놓고 그 안에 값만 바꿀 수 있음 (재할당)
# 변수는 그릇이라고 이해해면 좋음.

# 변수 이름 규칙
# 영어, 숫자, _(언더바) 만 사용 (한글도 되긴 하나 영어만 사용하는것을 추천. 대부분의 서버가 영어로 되어있고 한글은 없는경우도 있음)
# 제일 앞에는 *숫자*가 오면 안된다 (제일 앞에는 영어가 오는게 일반적. _는 보통 특별하게 사용하는 변수)
# name = "본인이름" -> name : 변수 이름, "__" : ""안의 내용이 변수의 값. ( 변수의 값을 할당하는 (공)식)
# 변수를 만들떄는 무조건 값의 할당이 이루어져야 함. 다음줄에 값 할당하기 안됨. 같은줄에 반드시
# 키워드 사용 불가 (오류방지) -> 키워드: 파이썬에서 정해놓은 프로그래밍 단어들
# ex) if -> 파이썬 내에서 사용하는 함수.  변수로 if를 만들 수 없음. (if=3 -> 이런거 불가)

# 문자형 변수
# name="황혜리" -> 출력해보기
# name="황혜리"
first_name="혜리"
last_name="황"
name=last_name+first_name # 더하기 연산자 사용
print(name)
# 변수 값을 수정해서 다른 이름을 만들 수 있음.

# 숫자형 변수
a=6 # 변수를 만들고 값을 할당함.
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)

# print("안녕하세요") -> 안녕하세요 는 상수. 한번 쓰면 다음에 다시 재사용 불가. 매번 재입력.
# ptint("2") -> 2는 상수. 다음에 재사용 불가 매번 재 입력 필요.
# 변수 : 한번 써도 다음에 재 사용 가능. 반복 사용 할떄 유용