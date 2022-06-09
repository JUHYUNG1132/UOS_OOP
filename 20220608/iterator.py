class myNumber:
    def __init__(self):
        self.a = None

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        if x > 100:
            raise StopIteration
        return x

myclass = myNumber()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

for i in myclass:
    print(i)