# 제목: 제08장 프로그래밍 문제 04번
# 설명: 클래스
# 파일이름: 08장04번.py
# 수정날짜: 2022년5월30일
# 작성자: 이주형

class Rectangle:
    def __init__(self, x, y, w, h):
        self.__x = x
        self.__y = y
        self.__width = w
        self.__height = h

    def __str__(self):
        return "좌표 = ({}, {}), 크기 = {}".format(self.__x, self.__y, self.__width * self.__height)

    def setX(self, x):
        self.__x = x

    def getX(self):
        return self.__x

    def setY(self, y):
        self.__y = y

    def getY(self):
        return self.__y

    def setW(self, w):
        self.__width = w

    def getW(self):
        return self.__width

    def getH(self, h):
        self.__height = h

    def getH(self):
        return self.__height

    def getArea(self):
        return self.__height * self.__width / 2

    def overlap(self, r):
        if (self.__x < r.getX() < self.__x + self.__height) and (self.__y < r.getY() < self.__y + self.__height):
            print("r1과 r2는 서로 겹칩니다.")


r1 = Rectangle(0, 0, 100, 100)
r2 = Rectangle(10, 10, 100, 100)
r1.overlap(r2)
