#제목: 제5장 프로그래밍 문제 16번
#설명: 함수 작성
#파일이름: 05장16번.py
#수정날짜: 2022년4월5일
#작성자: 이주형

import turtle as t

def draw_line():
    t.forward(100)
    t.backward(100)
    
for i in range(12):
    draw_line()
    t.left(30)