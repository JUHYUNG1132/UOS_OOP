#제목: 제07장 프로그래밍 문제 08번
#설명: 자료구조
#파일이름: 07장08번.py
#수정날짜: 2022년4월25일
#작성자: 이주형

d = {1:'January', 2:'Febuary', 3:'March', 4:'April', 5:'May',
     6:'June', 7:'July', 8:'August', 9:'September', 10:'October',
     11:'November', 12:'December'}

ind = int(input("달의 번호: "))
if ind in d:
    print('달의 이름:',d.get(ind))