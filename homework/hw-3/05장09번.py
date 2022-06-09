#제목: 제5장 프로그래밍 문제 9번
#설명: 유클리드 호제법
#파일이름: 05장09번.py
#수정날짜: 2022년4월5일
#작성자: 이주형

def euclid(n1,n2):
    max = n1 if n1>=n2 else n2
    min = n2 if n2<=n1 else n1
    if min ==0:
        return max
    return euclid(max%min, min)
    
n1 = int(input("첫 번째 정수를 입력하시오: "))
n2 = int(input("두 번째 정수를 입력하시오: "))

print(euclid(n1,n2))