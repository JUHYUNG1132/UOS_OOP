#제목: 제5장 프로그래밍 문제 15번
#설명: 함수 작성
#파일이름: 05장15번.py
#수정날짜: 2022년4월5일
#작성자: 이주형

import turtle as t

def draw_square(size):
    for i in range(4):
        t.fd(size)
        t.left(90)
        size += 5
    draw_square(size)
    
draw_square(1)