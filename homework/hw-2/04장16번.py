#제목: 제4장 프로그래밍 문제 16번
#설명: 반복
#파일이름: 04장16번.py
#수정날짜: 2022년3월29일
#작성자: 이주형


size = int(input("게임판의 크기: "))

horiz = " --- "
verti = "|   |"
for i in range(size):
    print(horiz*size)
    print(verti*size)
    print(verti*size)
print(horiz*size)
