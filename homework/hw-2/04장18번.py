#제목: 제4장 프로그래밍 문제 18번
#설명: 난수 원
#파일이름: 04장18번.py
#수정날짜: 2022년3월29일
#작성자: 이주형

import random
import turtle as t

for i in range(10):
    pos = [random.randint(-100,100),random.randint(-100,100)]
    rad = random.randint(10,100)
    t.penup()
    t.setposition(pos)
    t.pendown()
    t.circle(rad)   
    