#제목: 제5장 프로그래밍 문제 8번
#설명: 함수 작성
#파일이름: 05장08번.py
#수정날짜: 2022년4월5일
#작성자: 이주형

digi = ["천", "백", "십", ""]
cnt = ["영", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
slice = list()                          #문자로 변환된 결과 저장 리스트
digiInd = 3                             #자릿수를 지정하는 인덱스
def getMoneyText(amount):
    global digiInd                      #전역변수 digiInd 사용
    if amount % 10:
        slice.append(cnt[amount % 10] + digi[digiInd])          #1의자리부터 계산
    digiInd -= 1
    exchange = amount // 10                                     #10으로 나눔(그다음 자릿수로 넘어감)
    if exchange == 0:                                           #그다음 자릿수가 없으면 결과 출력
        for a in reversed(slice):
            print(a, end = " ")
        print("\b원")
    else:
        getMoneyText(exchange)                                  #10으로 나눈 몫을 인수로 다시 계산
        
inp = int(input("1000 이하의 금액을 입력하시오: "))
getMoneyText(inp)