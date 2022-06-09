# 파이썬 리스트 클래스를 상속받아 스택 구현
# 코드 재사용(code reuse)
class Stack(list):
    def push(self, data):
        self.append(data)


s = Stack()
s.push(1)
s.push('test')
s.push([1, 2, 3])
print(s)
print(s.pop())
print(s)
