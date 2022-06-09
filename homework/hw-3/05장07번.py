#제목: 제5장 프로그래밍 문제 7번
#설명: 조건 함수
#파일이름: 05장07번.py
#수정날짜: 2022년4월5일
#작성자: 이주형

def getIntRange(a,b):
    inp = int(input())
    return (inp if a <= inp and inp <= b else "F")

print("날짜를 입력하시오(월과 일")
while(True):
    print("월을 입력하시오(1부터 12사이의 값): ", end="")
    mon = getIntRange(1,12)
    if mon == "F":
        continue
    else:
        break
while(True):
    print("일을 입력하시오(1부터 31사이의 값): ", end="")
    day = getIntRange(1,31)
    if day == "F":
        continue
    else:
        break
print("입력된 날짜는 {}월 {}일 입니다".format(mon, day))
    