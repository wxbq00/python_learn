from random import randint
chinese=[randint(60,100) for x in range(10)]
math=[randint(60,100) for x in range(10)]
english=[randint(60,100) for x in range(10)]
total=[]
for c,m,e in zip(chinese,math,english):
    total.append(c+m+e)
print(total)


from itertools import chain
a1=[randint(60,100) for x in range(10)]
a2=[randint(60,100) for x in range(10)]
a3=[randint(60,100) for x in range(10)]
count=0#计数
print(a1,a2,a3)
for x in chain(a1,a2,a3):
    if x>90:
        count+=1
print(count)
#如何在一个for语句中迭代多个可迭代对象zip/itertools.chain
#内置函数zip,能将多个可迭代对象合并，每次迭代返回一个元组
#使用标准库中的itertools.chain，它能将多个可迭代对象连接
