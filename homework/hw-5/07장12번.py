#제목: 제07장 프로그래밍 문제 12번
#설명: 자료구조
#파일이름: 07장12번.py
#수정날짜: 2022년4월25일
#작성자: 이주형


s = input("문자열을 입력하시오: ")
b = input("금지어를 입력하시오: ")
for ind, word in enumerate(s.split()):
    for wordB in b.split():
        if word == wordB:
            for i in range(len(word)):
                word = word.replace(word[i], "*")
            print(word, end=' ')
        else:
            print(word, end= ' ')