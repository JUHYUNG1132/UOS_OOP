#제목: 제4장 프로그래밍 문제 05번
#설명: 반복문
#파일이름: 04장05번.py
#수정날짜: 2022년3월28일
#작성자: 이주형

for i in range(1, int(input("정수를 입력하시오: "))+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print("")