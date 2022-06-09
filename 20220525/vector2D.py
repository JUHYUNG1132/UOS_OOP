
# python 에서 모든 클래스는 object 클래스를 상속함

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, v):
        a = self.x + v.x     # <= 덕 타이핑
        b = self.y + v.y
        return Vector2D(a, b)

    def __add__(self, v):
        return Vector2D(self.x + v.x, self.y + v.y)

    def sub(self, v):
        a = self.x - v.x
        b = self.y - v.y
        return Vector2D(a, b)

    def __str__(self):
        print('__str__메소드')
        # return f"{self.x}, {self.y}"
        return '(%g, %g)' % (self.x, self.y)


a = Vector2D(1, 2)
b = Vector2D(3, 4)
c = a.add(b)
print(c)
print(a+b)
