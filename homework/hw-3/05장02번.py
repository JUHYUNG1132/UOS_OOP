#제목: 제5장 프로그래밍 문제 2번
#설명: 함수 작성
#파일이름: 05장02번.py
#수정날짜: 2022년4월5일
#작성자: 이주형

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

n1 = int(input("첫 번째 정수를 입력하시오: "))
n2 = int(input("두 번째 정수를 입력하시오: "))

print(f"({n1} + {n2} = {add(n1,n2)})")
print(f"({n1} - {n2} = {sub(n1,n2)})")
print(f"({n1} * {n2} = {mul(n1,n2)})")
print(f"({n1} / {n2} = {div(n1,n2)})")