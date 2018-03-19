#如何将多个小字符串拼接成一个大的字符串字符串(+)/S.join()
p=['a','b','c']
s=''
for i in p:
    s+=i
print(s)
print(''.join(str(x) for x in p))
