'''
num=[2,3,4,5]
result=list(map (lambda x:x%2==0,num))
print(result)'''
from functools import reduce

'''
from functools import reduce

num=[1,2,3,4,5,6,67,734,23,12,123,123,123,4531,12,123,421,123,122,1222,1233,2112,2312231,23123,212312,12355,6]
result=reduce(lambda a,b:a+b,num)
print(result)
'''

price=[123,1223,12223,1223,12255,2212]

result=list(filter(lambda x: x>2000,price))
Total=reduce(lambda a,b : a+b,result)
print(Total)