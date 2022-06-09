a = 10
aa = id(a)
a = 20
aaa = id(a)
print(aa)
print(aaa)

#불변객체는 인터닝을 함
a = 10
b = 10
print('integer =', id(a) == id(b))
a = 10.1
b = 10.1
print('float =', id(a) == id(b))
a = '10'
b = '10'
print('string =', id(a) == id(b))
#가변객체는 인터닝을 하지 않음
a = [1,2]
b = [1,2]
print('list= ', id(a) == id(b))

#operator == vs is
a = [1,2]
b = [1,2]
print(a is b) # id(a) == id(b)
print(a == b) # a 내용물 == b 내용물
