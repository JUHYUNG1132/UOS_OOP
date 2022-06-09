

class Animal:
    def __init__(self, str):
        self.name = str                  # name 이라는 인스턴스 변수 정의
        
    def sing(self):
        print(f'animal {self.name} sings!')
        

###########자식 클래스 정의##################
class Dog(Animal):                       # Dog 클래스는 Animal을 상속받음
    def __init__(self, str, brd):
        super().__init__(str)            #super() 내장함수는 부모클래스의 객체를 반환한다.
        self.breed = brd                # 자식이 인스턴스 변수를 추가
        
    def sing(self):
        print(f'dog {self.name} with {self.breed} sings!!')#메소드 재정의(오버라이드, override)
    
    
        
class Cat(Animal):
    def __init__(self, str, n):
        super().__init__(str)
        self.leng = n
        
    def sing(self):
        print(f'cat {self.name} with 수염길이 {self.leng} sings!!!')
            
        
a = Animal('동물')
d = Dog('개', '치와와')
c = Cat('나비', 5)
a.sing()
d.sing()                                 # 모든 속성, 동작 상속받음
c.sing()