from random import randint
d={x:randint(60,100) for x in range(1,21)}
print(d)
c={k:v for k,v in d.items() if v>=90}
print(c)
data=[randint(-10,10) for x in range(10)]
s=set(data)#集合
e={x for x in s if x%3==0 }
print(e)
#数据筛选
print(randint(1,100))#随机整数
