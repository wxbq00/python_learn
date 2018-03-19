#如何去掉字符串中不需要的字符
# 方法一,字符串strip() lstrip() rstrip() 去掉字符串两端字符
# 方法二,删除单个位置的字符,可以使用切片 + 拼接的方式
# 方法三,字符串的replace()方法或者正则表达式re.sub删除任意位置字符
# 方法四,字符串translate方法,可以同时删除多种不同的字符
s='--abc++'
print(s.strip('-+'))
print(s[2:5])
import re
print(re.sub(r'[\-,\+]','',s))

