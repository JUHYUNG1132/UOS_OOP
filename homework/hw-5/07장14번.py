#제목: 제07장 프로그래밍 문제 14번
#설명: 문자배열
#파일이름: 07장14번.py
#수정날짜: 2022년4월25일
#작성자: 이주형

s = input()
d = list()
print(s, end=' -> ')
for att in s.split('/'):
    d.append(att)
print("".join(str(d[2])+str(d[0])+str(d[1])))