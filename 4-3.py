#如何调整字符串中文本格式re.sub(p,r'\1/\2',str1)/re.sub('(?P<Name>p),'\g<Name>',str1)
s = "2017-01-22"
import re
print (re.sub("(\d{4})-(\d{2})-(\d{2})",r"\2/\3/\1",s))
