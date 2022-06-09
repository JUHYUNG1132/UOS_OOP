# 제목: 제12장 프로그래밍 문제 01번
# 설명: 상속
# 파일이름: 12장01번.py
# 수정날짜: 2022년5월30일
# 작성자: 이주형

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)


a = Point3D(1, 2, 3)
print(a)
