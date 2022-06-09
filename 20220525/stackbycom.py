
# 파이썬 리스트 클래스를 composition으로 스택 구현
class Stack(list):
    def __init__(self):
        self.lst = []

    def pop(self):
        return self.lst.pop()

    def push(self, data):
        self.lst.append(data)


s = Stack()
s.push(1)
s.push('test')
s.push([1, 2, 3])
print(s)
print(s.pop())
print(s)
