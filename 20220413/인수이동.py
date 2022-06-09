def change(x):
    print(id(x))
a = 100
change(a)
print(id(a))

def listchange(lst):
    lst[0] = 'moon'
    
a = [1,2]
listchange(a)
print(a)