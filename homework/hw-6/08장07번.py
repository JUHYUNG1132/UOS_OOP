# 제목: 제08장 프로그래밍 문제 07번
# 설명: 클래스
# 파일이름: 08장07번.py
# 수정날짜: 2022년5월30일
# 작성자: 이주형

class PhoneBook:
    def __init__(self):
        self.__contacts = dict()

    def __str__(self):
        res = ""
        for key, val in self.__contacts.items():
            res += key + "\n"
            for skey, sval in val.items():
                if sval:
                    res += str(skey) + ": " + str(sval) + "\n"
        return res

    def add(self, name, mobile=None, office=None, email=None):
        self.__contacts[name] = {'mobile': mobile, 'office phone': office, 'email': email}


obj = PhoneBook()
obj.add('lee', mobile='123456', email='jeff@naver.com', office='1425')
obj.add('kim', mobile='123456', email='jeff@naver.com')

print(obj)
