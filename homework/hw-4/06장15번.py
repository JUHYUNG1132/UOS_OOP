#제목: 제06장 프로그래밍 문제 15번
#설명: 확률
#파일이름: 06장15번.py
#수정날짜: 2022년4월17일
#작성자: 이주형

import random

comp = [0,1]
lst = [random.choice(comp) for i in range(10)]
cntlst=list()
cnt =0
maxcnt=0
maxind=0

for i in range(0,len(lst)):
    if i== len(lst)-1:
            if maxcnt < cnt+1:
                maxcnt = cnt+1
                maxind = i-cnt
    else:
        if lst[i] == lst[i+1]:
            cnt+=1
        else:
            if maxcnt < cnt+1:
                maxcnt = cnt+1
                maxind = i-cnt
            cnt=0
      
print(lst)
print("최대 연속 =", maxind, "부터", maxcnt, "개")