#제목: 제5장 프로그래밍 문제 14번
#설명: 제곱근 추정
#파일이름: 05장14번.py
#수정날짜: 2022년4월5일
#작성자: 이주형

def test(x,y):
    temp = x/y
    if int((temp-y)*1000000)==0:
        print(temp)
    else:
        test(x,(temp+y)/2)


test(2,1)   