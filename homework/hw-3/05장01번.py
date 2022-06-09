#제목: 제5장 프로그래밍 문제 1번
#설명: 둘레 구하기
#파일이름: 05장01번.py
#수정날짜: 2022년4월5일
#작성자: 이주형

from math import pi

def get_peri(rad = 5.0):
    return 2*pi*rad

print(f"get_peri() = {get_peri()}")
print(f"get_peri(4.0) = {get_peri(4)}")