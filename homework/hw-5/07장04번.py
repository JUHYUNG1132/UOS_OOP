#제목: 제07장 프로그래밍 문제 04번
#설명: 자료구조-딕셔너리
#파일이름: 07장04번.py
#수정날짜: 2022년4월25일
#작성자: 이주형

from yaml import scan

d = {x:x*10 for x in range(1,7)}
ind = int(input("키를 입력하시오: "))
if ind in d:
    print("키 {}는 딕셔너리에 있습니다".format(ind))