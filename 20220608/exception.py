class myExcep(Exception):
    def __str__(self):
        return "My Exception!"

try:
    print('hello')
    #print(x)
    print('world')
    raise myExcep

except Exception as e:
    print(e)

except myExcep as e:
    print(e)

else:
    print('정상실행')

finally:
    print('EOP')

