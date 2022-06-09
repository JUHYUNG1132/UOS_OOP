#제목: 제06장 프로그래밍 문제 14번
#설명: 지뢰찾기
#파일이름: 06장14번.py
#수정날짜: 2022년4월17일
#작성자: 이주형

import random

def showlst(arr):
    for i in arr:
        for j in i:
            print(f"{j:^3}", end="")
        print()

arr = [["." for i in range(10)] for i in range(10)]
for i in range(10):
    for j in range(10):
        if random.random()<0.3:
            arr[i][j] = "#"
showlst(arr)