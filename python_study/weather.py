# 4월 18일 4
# 수업 5 ---------------------------------------------
#       <<<     실      습      >>>
print("연산자 실습해보기 1")
weather="비"  # weather 변수에 값 할당
print("비가 오나요?", weather=="비")  # weather가 "비" 와 같을때 결과값인True가 출력. "비가 오나요?" 문장에 "비"가 있으므로 true 출력
if weather=="비":   # weather의 값이 "비"와 같으면 조건식이 True이므로 만족. 코드블록 실행
    print("우산을 가져간다")
else:   # 조건식이 False 이면 실행
    print("우산을 가져가지 않은다")  # 여기는 실행되지 않음.


#       <<<     실      습      >>>
print("연산자 실습해보기 2")
weather="맑음"  # weather 변수에 값 할당
print("비가 오나요?", weather=="비")  # weather가 "비" 와 같을때 결과값인True가 출력. "비가 오나요?" 문장에 "비"가 있으므로 true 출력
if weather=="비":   # weather의 값이 "비"와 같으면 조건식이 False이므로 불만족. 코드블록 실행 안됨
    print("우산을 가져간다")
elif weather=="맑음":
    print("날씨가 좋다")
else:   # 조건식이 False 이면 실행
    print("우산을 가져가지 않은다")  # 여기는 실행되지 않음.