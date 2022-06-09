#제목: 제2장 프로그래밍 문제 6번
#설명: 팁 계산
#파일이름: 02장06번.py
#수정날짜: 2022년3월20일
#작성자: 이주형
fcost = int(input("음식 비용: "))
trate = int(input("팁 비율:   %\b\b\b"))
print("총 비용: ", int(fcost*(1+trate/100)))