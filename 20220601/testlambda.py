
def sum(x, y): return x+y


# 우변의 람다식은 함수 객체의 레퍼런스를 반환함
fsum = lambda x, y: x+y
fsub = lambda x, y: x-y

print('the sum is ', fsum(1, 3))  # => 함수의 이름은 레퍼런스를 반환
print('the sum is ', sum(1, 3))

def op(fcn, a, b):
    return fcn(a, b)

# 함수객체의 레퍼런스를 인수로 사용할 수 있다.
print(op(fsum, 100, 10))
print(op(fsub, 100, 10))

# 특정 값을 매개변수에 곱하는 함수를 반환하는 함수
def ff(x):
    f = (lambda a: a*x)
    return f
# 기존 함수의 경우 함수로 새로운 함수를 반환할 수 있나??


f10 = ff(10)   # ff에서 f의 x값이 10인 함수를 반환
f100 = ff(100)   # ff에서 f의 x값이 100인 함수를 반환
print(f10(2), f100(2))
# 함수 레퍼런스로 호출 2
print((lambda a: a*10)(10))
# 디폴트인수도 지정가능
print((lambda x=100: x+1)())
