#제목: 제4장 프로그래밍 문제 17번
#설명: 반복문
#파일이름: 04장17번.py
#수정날짜: 2022년3월29일
#작성자: 이주형

for i in range(10):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print("*")
        