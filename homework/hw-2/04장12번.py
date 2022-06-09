#제목: 제4장 프로그래밍 문제 12번
#설명: 파이값 계산
#파일이름: 04장12번.py
#수정날짜: 2022년3월28일
#작성자: 이주형

import random

def lenCalc(posx,posy):  #원점으로부터 거리 구하는 함수
    return (posx**2+posy**2)**0.5

pos = list()
hit = 0

for i in range(1000000):  #-1부터 1까지의 난수 100만개 생성, 2차원 pos리스트에 저장 y축은 좌표 순서, x축은 xy값
    pos.append([random.uniform(-1,1),random.uniform(-1,1)])
    if lenCalc(pos[i][0], pos[i][1])<1:
        hit += 1
print(f"파이의 값은 {4*hit/len(pos)}")