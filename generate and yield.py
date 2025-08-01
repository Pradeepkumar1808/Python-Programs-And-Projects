def getnum(n):
    for i in range(n):
        yield i

for num in getnum(10):
    print(num)