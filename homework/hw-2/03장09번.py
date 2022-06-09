#제목: 제3장 프로그래밍 문제 9번
#설명: 시간 계산
#파일이름: 03장09번.py
#수정날짜: 2022년3월26일
#작성자: 이주형

import random

a = random.randint(1,100)
b = random.randint(1,100)
c = random.randint(0,3)
ope = ["+", "-", "*", "/"]

if c == 0:
    print("맞았습니다" if int(input("{} {} {}의 값은? ".format(a,ope[c],b))) == (a+b) else "틀렸습니다")
elif c == 1:
    print("맞았습니다" if int(input("{} {} {}의 값은? ".format(a,ope[c],b))) == (a-b) else "틀렸습니다")
elif c == 2:
    print("맞았습니다" if int(input("{} {} {}의 값은? ".format(a,ope[c],b))) == (a*b) else "틀렸습니다")
else :
    print("맞았습니다" if int(input("{} {} {}의 값은? ".format(a,ope[c],b))) == (a/b) else "틀렸습니다")