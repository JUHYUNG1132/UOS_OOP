import math

def myFcn(fcn):
    return lambda x: fcn(x)

print(math.cos(0))
mysine = myFcn(math.sin)
print(mysine(math.pi/2))

##############################################

a = [1,2,34]
print(*a)
a = {'one':'1', 'two': 2,'three': 3}
print(*a)