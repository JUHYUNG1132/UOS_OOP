#제목: 제07장 프로그래밍 문제 10번
#설명: 자료구조
#파일이름: 07장10번.py
#수정날짜: 2022년4월25일
#작성자: 이주형

s1 = {10,20,30,40,50,60}
s2 = {30,40,50,60,70,80}
print('어느 한쪽에만 있는 요소들', sorted((s1-s2).union(s2-s1)))