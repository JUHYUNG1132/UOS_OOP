#제목: 제4장 프로그래밍 문제 07번
#설명: 반복문
#파일이름: 04장07번.py
#수정날짜: 2022년3월28일
#작성자: 이주형

import turtle as t
import math

for degree in range(361):
    
    t.setposition(degree,math.sin(degree*math.pi/180)*100)