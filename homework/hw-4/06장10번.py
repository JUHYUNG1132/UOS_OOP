#제목: 제06장 프로그래밍 문제 10번
#설명: 리스트 + 터틀
#파일이름: 06장10번.py
#수정날짜: 2022년4월17일
#작성자: 이주형

import turtle as t
import random
lst = ["red", "yellow", "blue", "purple"]

def draw_square(x,y,c):
    t.color(c)
    t.begin_fill()
    t.fd(x)
    t.left(90)
    t.fd(y)
    t.left(90)
    t.fd(x)
    t.left(90)
    t.fd(y)
    t.left(90)
    t.end_fill()
    
for i in lst:
    t.pendown()
    draw_square(50,50,i)
    t.penup()
    t.goto(random.randint(-200,200),random.randint(-200,200))

t.mainloop()