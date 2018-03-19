from collections import namedtuple
name,age,sex,email=range(4)
Student=namedtuple('Student',['name','age','sex','email'])#可以访问元祖里面的每一个元素
s=Student('jim',21,'male','sad@qq.com')
print(s.name)#为元素命名
#如何为元组中的每个元素命名, 提高程序可读性-collections.namedtuple