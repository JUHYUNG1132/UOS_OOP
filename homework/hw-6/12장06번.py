# 제목: 제12장 프로그래밍 문제 06번
# 설명: 상속
# 파일이름: 12장06번.py
# 수정날짜: 2022년5월30일
# 작성자: 이주형

class Course:
    def __init__(self, course, credit):
        self.course = course
        self.credit = credit
        self.std = list()

    def __str__(self):
        return "{}과목 수강생 = {}".format(self.course, self.std)

    def addStd(self, info):
        self.std.append(info)


class Department:
    def __init__(self, dept):
        self.dept = dept
        self.course = list()

    def __str__(self):
        return "{}학과 개설과목 = {}".format(self.dept, self.course)

    def addCourse(self, course, credit):
        self.course.append([course, credit])
        return Course(course, credit)


class Student:
    def __init__(self, name, sID):
        self.name = name
        self.sID = sID

    def __str__(self):
        return "학생 이름 = {}, 학번 = {}".format(self.name, self.sID)

    def enroll(self, course):
        course.addStd([self.name, self.sID])


a = Department('컴퓨터')
math1 = a.addCourse('공학수학', 2)
math2 = a.addCourse('이산수학', 3)

kim = Student('kim', 1234567890)
lee = Student('이주형', 2021440099)
lee.enroll(math1)
kim.enroll(math2)

print(math1.std, math2.std)
print(a.course)
