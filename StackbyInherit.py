"""

상속을 이용한 Stack 클래스 구현

"""

class Stack(list):

    def __init__(self, i):
        super().__init__([i])

    def isEmpty(self):
        return len(self) == 0

    def size(self):
        return len(self)

    def clear(self):
        while not self.isEmpty():
            self.pop()

    def push(self, item):
        self.append(item)

    def pop(self):
        if not self.isEmpty():
            return super().pop(-1)          # pop함수를 재정의했으므로 super() 사용

    def peek(self):
        if not self.isEmpty():
            return self.__str__()[-2]       # return 하면, [] 까지 문자열이므로 인덱스가 -1이 아닌 -2이다

s = Stack(1)
s.push(3)
print(s)
print(len(s))
print(s.isEmpty())
print(s.peek())
print(s.pop())
