

fruits = ()
fruits = ('apple', 'banana', 'grape')
cities = 'seoul', 'busan'       # 괄호가 없어도 됨

print(fruits)
print(cities)

fruits += (3,)            # 원소 하나짜리 튜플을 만들 때는 끝에 , 붙여줘야함!!
print(id(fruits), end= " => ")
fruits += (2,1)
print(id(fruits))
print(fruits)
#########################################
t = (2,4,5)               #튜플 패킹
(s1, s2, s3) = t          #튜플 언패킹
print(t)
print(*t)
print(s1, s2, s3)
#########################################
def fcn():
    return 10,20
a,b = fcn()
print(a,b)