#제목: 제5장 프로그래밍 문제 11번
#설명: 함수 작성
#파일이름: 05장11번.py
#수정날짜: 2022년4월5일
#작성자: 이주형

def deci2bin(n):
    bin = list()
    while True:
        bin.append(n%2)
        n //= 2
        if n == 0:
            for a in reversed(bin):
                print(a, end="")
            break
    
inp = int(input("10진수: "))
deci2bin(inp)