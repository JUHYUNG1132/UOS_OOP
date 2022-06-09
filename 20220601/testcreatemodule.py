"""
모듈은 세기지 정의 가능
1. 변수
2. 함수
3. 클래스
"""

var = 10

def fnc(a):
    return a+1

class Cls:
    def __str__(self):
        return 'module Class'

name = __name__
# 직접 실행할때만 name 이 __main__임
if __name__ == '__main__':
    print(var)
    print(fnc(10))
    print(Cls())
