#제목: 제5장 프로그래밍 문제 12번
#설명: 다중 반환
#파일이름: 05장12번.py
#수정날짜: 2022년4월5일
#작성자: 이주형

def getSorted(x,y):
    max = x if x>=y else y
    min = y if y<=x else x
    return min,max

n1 = int(input("첫 번째 정수를 입력하시오: "))
n2 = int(input("두 번째 정수를 입력하시오: "))

print(getSorted(n1,n2))