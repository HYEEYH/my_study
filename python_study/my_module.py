# 4월 26일 5 -------------------------------------------------------------------------
# 모듈 가져올 파일


def add(a,b):
    return a+b

def sub(a,b):
    return a-b


# 다른 파이썬 파일에서 이 모듈을 불러올때 미리 써놓은 함수(테스트용함수) 실행 안하게 하는 방법
# 이 파이썬 파일을 실행할 땐 여기선 메인.
# 다른 파일에 임포트 되면 이 파일은 모듈이 됨.

if __name__ == "__main__":          # 이 파일이 메인으로 실행될 때
    print(add(1,2))
    print(sub(3,4))
else:
    print(__name__)


