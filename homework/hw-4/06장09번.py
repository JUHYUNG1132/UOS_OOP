#제목: 제06장 프로그래밍 문제 09번
#설명: 리스트 + 터틀
#파일이름: 06장09번.py
#수정날짜: 2022년4월17일
#작성자: 이주형

import turtle as t

aList = [10,20,30,40,50,60,70,80,90,100,120]

for i in aList:
    t.forward(i)
    t.backward(i)
    t.right(30)
t.mainloop()