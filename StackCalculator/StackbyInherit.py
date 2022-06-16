"""

상속을 이용한 Stack 클래스 구현
스택 계산기용으로 수정
 - 스택의 입구를 첫 index로 바꿈

"""

class Stack(list):

    # def __init__(self):
    #     super().__init__()

    def isEmpty(self):
        return len(self) == 0

    def size(self):
        return len(self)

    def clear(self):
        while not self.isEmpty():
            self.pop()

    def push(self, item):
        self.insert(0, item)

    def pop(self):
        if not self.isEmpty():
            return super().pop(0)          # pop함수를 재정의했으므로 super() 사용

    def peek(self):
        if not self.isEmpty():
            return self.__str__()[2]       # return 하면, [] 까지 문자열이므로 인덱스가 -1이 아닌 -2이다

if __name__ == '__main__':
    s = Stack()
    print(s)
    for i in range(10):
        s.push(i)
    print(s)
    print(len(s))
    print(s)
    print(s.isEmpty())
    print(s.peek())
    print(s)
    print(s.pop())
    print(s)
    s.clear()
    print(s)
