#제목: 제06장 프로그래밍 문제 01번
#설명: 리스트 생성
#파일이름: 06장01번.py
#수정날짜: 2022년4월17일
#작성자: 이주형

indNum = int(input("입력할 값의 개수: "))
lst = list()
for ind in range(indNum):
    lst.append(int(input()))
print("값의 합계=", sum(lst))