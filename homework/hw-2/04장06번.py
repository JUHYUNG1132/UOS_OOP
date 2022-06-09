#제목: 제4장 프로그래밍 문제 06번
#설명: 반복문
#파일이름: 04장06번.py
#수정날짜: 2022년3월28일
#작성자: 이주형

import math


print("각도   sin값  cos값")
for degree in range(0,100,10):
    radian = 3.14 * degree / 180
    print("{:-.3f}  {:-.3f}  {:-.3f}".format(degree, math.sin(radian), math.cos(radian)))