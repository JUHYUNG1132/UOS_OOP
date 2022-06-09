class MyList:
    refCount = 0
    
    def __init__(self, alist):
        self.list = alist
        self.__list = alist #조건이 있는 초기값을 설정할 떄 private 사용
                            #여기서는 리스트가 조건, 중간에 변경되지 않게 만듬
        MyList.refCount += 1
    def findMinIndex(self, i):
        minIndex = i
        for k in range(i, len(self.__list)):
            if self.__list[minIndex] > self.__list[k]:
                minIndex = k
        return minIndex
    
    def swapElement(self, i, j):
        self.__list[i], self.__list[j] = self.__list[j], self.__list[i]
    
    def selectionSort(self):
        for i in range(len(self.__list)):
            self.swapElement(i, self.findMinIndex(i))
        return self.__list
    
    def showList(self):
        print(self.__list)
    
a = [9,1,6,8,4,3,2,0]
b = MyList(a)
print(".")
print(b.selectionSort())

print("private 변수")
b.showList()
try:
    print(b.__list)
except AttributeError as e:
    print("읽기 에러,", e)
    
print("클래스 사용 횟수", MyList.refCount)