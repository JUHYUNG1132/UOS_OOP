#제목: 제06장 프로그래밍 문제 13번
#설명: 리스트 좌표
#파일이름: 06장13번.py
#수정날짜: 2022년4월17일
#작성자: 이주형

def showlst(arr):
    print("-"*32)
    for i in range(1,11):
        print(f"{i:3}", end="")
    print("\n"+"-"*32)
    for i in arr:
        for j in i:
            print(f"{j:>3}", end="")
        print()

arr = [[0 for i in range(10)] for i in range(10)]

showlst(arr)
x = int(input("원하시는 좌석의 행번호를 입력하세요(종료는 -1)= "))
if x==-1:
    exit()
y = int(input("원하시는 좌석의 열번호를 입력하세요(종료는 -1)= "))
if y==-1:
    exit()
try:
    arr[y-1][x-1] = 1
    print("예약되었습니다.")
except:
    print("예약하지 못했습니다.")
showlst(arr)