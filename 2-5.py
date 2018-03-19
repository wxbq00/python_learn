#找到多个字典的公共健
from random import randint,sample
from functools import reduce
from six import viewkeys

s1={x:randint(1,4) for x in sample('abcdefg',randint(1,6))}#数量1-4个，abcdefg中去1-6个
s2={x:randint(1,4) for x in sample('abcdefg',randint(1,6))}
s3={x:randint(1,4) for x in sample('abcdefg',randint(1,6))}
#print(reduce(lambda a,b:a&b,map(dict.viewkeys,[s1,s2,s3])))


for k in s1:
    if k in s2.keys() and k in s3.keys():
        print(k)

print(s1,s2,s3)


