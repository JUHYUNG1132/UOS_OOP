#제목: 제3장 프로그래밍 문제 3번
#설명: 문자 처리
#파일이름: 03장03번.py
#수정날짜: 2022년3월26일
#작성자: 이주형

alp = input("문자를 입력하시오: ")
if alp == "r" or alp == "R":
    print("Rectangle")
elif alp == "t" or alp == "T":
    print("Triangle")
elif alp == "c" or alp == "C":
    print("Circle")
else:
    print("Unknown")
