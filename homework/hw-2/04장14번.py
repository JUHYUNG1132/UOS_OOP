#제목: 제4장 프로그래밍 문제 14번
#설명: 정수 계산
#파일이름: 04장14번.py
#수정날짜: 2022년3월29일
#작성자: 이주형

def isPrime(num):
    for i in range(2, num//2+1):
        if num%i==0:
            return
    print(num, end = " ")
        
        
prime = list()
for i in range(2,21):
    isPrime(i)
    