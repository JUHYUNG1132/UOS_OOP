#제목: 제07장 프로그래밍 문제 16번
#설명: 암호생성
#파일이름: 07장16번.py
#수정날짜: 2022년4월25일
#작성자: 이주형

import string
import random

s = "".join(string.ascii_letters + string.punctuation + string.digits)
pw=""
for i in range(8):
    pw += random.choice(s)

print(pw)