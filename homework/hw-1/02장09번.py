#제목: 제2장 프로그래밍 문제 9번
#설명: 정수 계산
#파일이름: 02장09번.py
#수정날짜: 2022년3월20일
#작성자: 이주형

num = int(input("정수: ")) 
sum = 0

for i in range(4):
    sum += num%10
    num //= 10
print(sum)