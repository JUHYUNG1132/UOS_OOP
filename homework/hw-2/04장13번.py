#제목: 제4장 프로그래밍 문제 13번
#설명: 피보나치 수열
#파일이름: 04장13번.py
#수정날짜: 2022년3월29일
#작성자: 이주형
    
n = int(input("몇 항까지 구할까요? "))

a = 0
b = 0
c = 1

for i in range(n):
    print(c ,end= ", ")
    a = b
    b = c
    c = a+b