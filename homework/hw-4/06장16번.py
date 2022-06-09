#제목: 제06장 프로그래밍 문제 16번
#설명: 소수 판별
#파일이름: 06장16번.py
#수정날짜: 2022년4월17일
#작성자: 이주형

lst = [i for i in range(2,101)]

for i in lst:
    for j in lst:
        if i==j:
            continue
        else:
            if j%i==0:
                lst.remove(j)
print(lst)