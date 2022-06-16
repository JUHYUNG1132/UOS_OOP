import os
import datetime

hwNum = str(input("hw 번호= "))
tChap = int(input("장 번호= "))
tTopic = str(input("장 주제= "))
pNum = int(input("문제 갯수= "))

dir = "C:/Users/jeff0/Desktop/과제/OOPPython이주형2021440099/homework/hw-{}".format(hwNum)

try:
    if not os.path.exists(dir):
        os.makedirs(dir)
    else:
        print("폴더가 이미 존재합니다.")
        input()
        exit()
except:
    print("오류")
    input()
    exit()

tdate = datetime.datetime.now()
tyear = tdate.year
tmonth = tdate.month
tday = tdate.day

for ind in range(1, pNum+1):
    tFile = "C:/Users/jeff0/Desktop/과제/OOPPython이주형2021440099/homework/hw-{}/{:02}장{:02}번.py".format(hwNum, tChap, ind)
    f = open(tFile, "w", encoding= 'utf-8')
    form = f"""#제목: 제{tChap:02}장 프로그래밍 문제 {ind:02}번
#설명: {tTopic}
#파일이름: {tChap:02}장{ind:02}번.py
#수정날짜: {tyear}년{tmonth}월{tday}일
#작성자: 이주형

"""
    f.write(form)
    f.close()
    