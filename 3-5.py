# 如何对迭代器做切片操作itertools.islice(open("test.txt"),0,10),迭代器消耗
import itertools
la=[x for x in range(1,20)]
b=iter(la)
for i in itertools.islice(la,5,10):
    print(i)
