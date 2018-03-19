# 如何拆分含有多种分隔符的字符串
# 解决方案1:
# 使用str.split()方法，每次处理一种分隔符号
# 解决方案2:
# 使用正则表达式re.split()，一次性拆分字符串
s="ab;;;;;cd|efg|hi,,jkl|mn\topq;rst,uvw\txyz"
import re
result=[x for x in re.split(";|,|\||\t",s) if x]
print('result is %s'%result)

