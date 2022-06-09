#제목: 제5장 프로그래밍 문제 6번
#설명: 함수 작성
#파일이름: 05장06번.py
#수정날짜: 2022년4월5일
#작성자: 이주형
import random

def mkprob(n1,n2):
    oper = ["+", "-", "*", "/"]
    print("정수 {} {} {} 은(는)?".format(n1,oper[random.randint(0,3)], n2))

n1 = int(input("첫 번째 정수를 입력하시오: "))
n2 = int(input("두 번째 정수를 입력하시오: "))

mkprob(n1,n2)