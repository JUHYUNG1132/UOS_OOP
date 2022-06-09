#제목: 제06장 프로그래밍 문제 11번
#설명: 
#파일이름: 06장11번.py
#수정날짜: 2022년4월17일
#작성자: 이주형

import random
import turtle as t

die = [1,2,3,4,5,6]

one = t.Turtle()
one.color("blue")
one.shape("arrow")

two = t.Turtle()
two.up()
two.setposition([0,-50])
two.down()
two.color("red")
two.shape("turtle")

one.forward(random.choice(die)*10)
two.forward(random.choice(die)*10)

t.mainloop()