# 4월 18일 5
# 수업 5 ---------------------------------------------
#       <<<     실      습      >>>
print("연산자 실습해보기 3")
age = 19
money = 50000
chicken = 20000
beer = 10000
drink = 5000
if money >= chicken:
    print("치킨을 먹는다")
if money >= beer and age >=20:
    print("맥주를 먹는다")
if money >= drink:
    print("음료수를 먹는다")


# 위의 코드는 틀린코드. 돈계산은 안됨.
# age = 19
# money = 20000 # -> 돈이 2만원이니까 치킨과 음료수를 둘 다 먹을 순 없음. 치킨만 먹고 끝나야 함.
# chicken = 20000
# beer = 10000
# drink = 5000
# if money >= chicken:
#     print("치킨을 먹는다")
# if money >= beer and age >=20:
#     print("맥주를 먹는다")
# if money >= drink:
#     print("음료수를 먹는다")


# 틀린 코드 고쳐보기
print("틀린코드 고치기 연습")
print("내가 만들어본 코드")
age = 19
money = 20000
chicken = 20000
beer = 10000
drink = 5000
if money >= chicken:
    print("치킨을 먹는다")
if money - chicken >= beer + drink and age>=20:
    print("맥주를 먹지 않은다")
if money - chicken - beer > drink:
    print("음료수를 먹는다")
# 틀렸다!. 돈이 만원만 있을경우 음료수는 먹을 수 있으나 코드상에서는 출력이 안됨.
# 수정
# if money >= chicken:
#    print("치킨을 먹는다")
#    if money - chicken >= beer + drink and age>=20: -------> # 돈이 더 적을 경우에도 if문으로 써줘야 함.
#        print("맥주를 먹지 않은다")
#        if money - chicken - beer > drink:  -------> # 돈이 더 적을 경우에도 if문으로 써줘야 함.
#            print("음료수를 먹는다")
# 이런식으로 모든 경우의 수를 써줘야 함.
print("\n")

# 추천 답
print("추천 답 코드1")
age = 19
money = 20000
chicken = 20000
beer = 10000
drink = 5000
if money >= chicken:
    money = money - chicken
    print("치킨을 먹는다")
if money >= beer and age >=20:
    money = money - beer
    print("맥주를 먹는다")
if money >= drink:
    money = money - drink
    print("음료수를 먹는다")
print("\n")
print("추천 답 코드2 -> 틀림. 값이 중복으로 많음. elif 써줘야 함.")
age = 19
money = 20000
chicken = 20000
beer = 10000
drink = 5000
if money >= chicken+beer+drink and age>=20:
    print("치킨, 맥주, 음료수를 먹는다")
if money >= chicken+beer and age >=20:
    print("치킨과 맥주를 먹는다")
if money >= chicken + drink:
    print("치킨과 음료수를 먹는다")
if money>= chicken:
    print("치킨을 먹는다")
if money>= beer + drink and age>=20:
    print("맥주와 음료수를 먹는다")
if money >= drink:
    print("음료수를 먹는다")
print("\n")
print("추천 답 코드3 -> 답 코드2 수정.")
age = 19
money = 20000
chicken = 20000
beer = 10000
drink = 5000
if money >= chicken+beer+drink and age>=20:
    print("치킨, 맥주, 음료수를 먹는다")
elif money >= chicken+beer and age >=20:
    print("치킨과 맥주를 먹는다")
elif money >= chicken + drink:
    print("치킨과 음료수를 먹는다")
elif money>= chicken:
    print("치킨을 먹는다")
elif money>= beer + drink and age>=20:
    print("맥주와 음료수를 먹는다")
elif money >= drink:
    print("음료수를 먹는다")

print("\n")
