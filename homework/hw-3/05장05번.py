#제목: 제5장 프로그래밍 문제 5번
#설명: 패스워드 조건
#파일이름: 05장05번.py
#수정날짜: 2022년4월5일
#작성자: 이주형
#참고: https://jinisbonusbook.tistory.com/30 <=문자열 판별 함수

from tabnanny import check


def checkPass(p):
    if len(p)<8:        #길이가 8자리 이상인가?
        return 1
    if p.isalpha():     #알파벳으로만 구성됐나?
        return 2
    if p.isdecimal():   #숫자로만 구성됐나?
        return 3
    if p.isupper():     #대문자로만 구성됐나?
        return 4
    if p.islower():     #소문자로만 구성됐나??
        return 5
    return 0
    

pwd = input("패스워드를 입력하시오: ")

if checkPass(pwd):
    print("사용할 수 없습니다. 다시 입력하세요!")
else:
    print("사용할 수 있습니다.")
