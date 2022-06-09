#제목: 제5장 프로그래밍 문제 10번
#설명: 소수 판별
#파일이름: 05장10번.py
#수정날짜: 2022년4월5일
#작성자: 이주형

def testPrime(n):
    for i in range(2, n//2+1):
        if n%i == 0:
            return 0
    return 1

for i in range(2,100):
    if testPrime(i) == 1:
        print(i, end=" ")