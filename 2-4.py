#对字典里的项排序
from random import randint
d={x:randint(60,100) for x in 'abcdef'}
#print((99,'a')>(90,'b'))
print(sorted(zip(d.values(),d.keys())))#变成元祖来比较，按key比较
print(sorted(d.items(),key=lambda x:x[1]))#以第二个值来比较
#如何根据字典中值的大小，对字典中的项排序
print(dict(sorted(d.items(),key=lambda x:x[1])))

