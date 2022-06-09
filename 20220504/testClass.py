class Complex:
    classVar = 100
    
    def __init__(self, r, i):
        self.real = r
        self.imag = i
        self.pwd = 1111
        self.__pwd = 1112
        
    def printComplex(self):
        print(self.real,'+j', self.imag, end = "")
        print(", __pwd = {}".format(self.__pwd))
        
#############################
a = Complex(1,2)
b = Complex(3,4)
#############################
print(type(a))
a.printComplex()
print()
#############################
print(a.pwd)
# print(a.__pwd)
#############################
print(Complex.classVar)
a.classVar = 200
print(a.classVar, b.classVar)
Complex.classVar = 200
print(a.classVar, b.classVar)