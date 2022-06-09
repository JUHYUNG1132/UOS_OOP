############################################################################
# 동일한 객체에 대한 id값은 interning이 되는가?
#interning test case 1
a = 3
i = id(a)
ii = id(a)
print('정수 id값')
print("동일 값 =",i == ii)
print("동일 id =", i is ii, id(i), id(ii))
#id일 경우 interning이 안된다.
print()
#interning test case 2
a = [1,2]
i = id(a)
a.append(3)
ii = id(a)
print('리스트 id 값')
print("동일 값 =",i == ii)
print("동일 id =", i is ii)

print()
#interning test case 3-1                    인터넷) -5~256사이의 값을 제외하면 인터닝이 안된다?
i = 256
ii = 256
print('정수 값')
print("동일 값 =",i == ii)
print("동일 id =", i is ii)

print()
#interning test case 3-2
i1 = 1234512341231423
i2 = 1234512341231423
print('정수 값')
print("동일 값 =",i1 == i2)
print("동일 id =", i1 is i2)

print()
#interning test case 4
def fcn():
    return 10000

i = fcn()
ii = fcn()
print('return 값')
print("동일 값 =",i == ii)
print("동일 id =", i is ii, id(i), id(ii))

#############################################################################