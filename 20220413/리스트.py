temp = [1,2,3,4]
temp[2] = 300
print(temp)
for i in temp:
    print(i, end=', ')
print('')
#############################
heros = []
heros.append('ironmen')
actor = []
actor.append('로다주')

for i in zip(heros,actor):
    print(i)
#############################
heros = ['아이언맨', '토르', '헐크', '스칼렛 위치', '헐크']
n = heros.index('헐크')
print(heros)
print(n)
