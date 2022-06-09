#제목: 제5장 프로그래밍 문제 4번
#설명: 점수 분류
#파일이름: 05장04번.py
#수정날짜: 2022년4월5일
#작성자: 이주형

def getGrade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
print("성적은 {}입니다".format(getGrade(int(input("성적을 입력하세요: ")))))