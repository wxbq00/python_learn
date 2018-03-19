#查看序列中出现频率最高的元素
from random import randint
from collections import Counter
d=[randint(0,30) for _ in range(30)]#生产30个在0-30范围的数,序列

print(d)
c=Counter(d)#字典

print(c.most_common(3))#xx出现了x次