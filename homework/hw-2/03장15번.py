#제목: 제3장 프로그래밍 문제 15번
#설명: 배수 계산
#파일이름: 03장15번.py
#수정날짜: 2022년3월26일
#작성자: 이주형

imp = int(input("정수를 입력하세요: "))

if imp%15==0:
    print("Python Express")
elif imp%3 == 0:
    print("Python")
elif imp%5==0:
    print("Express")