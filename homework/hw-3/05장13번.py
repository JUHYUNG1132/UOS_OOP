#제목: 제5장 프로그래밍 문제 13번
#설명: 가위바위보
#파일이름: 05장13번.py
#수정날짜: 2022년4월5일
#작성자: 이주형

import random


def dice_game():
    print("=======  dice_game() 호출  =======")
    hm = random.randint(1,6)
    com = random.randint(1,6)
    print("인간: 주사위값= ", hm)
    print("컴퓨터: 주사위값= ", com)
    if hm>com:
        print("인간승리")
    elif hm==com:
        print("비김")
    else:
        print("컴퓨터승리")
    
while True:
    dice_game()
    print("=======  dice_game() 복귀  =======")
    if input("중단할까요? Y/N").lower() == "y":
        break