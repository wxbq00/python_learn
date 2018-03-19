import json
a=[1, 2, 'abc',{'name': 'doudou','age': 13}]
print(json.dumps(a))#将一个python对象转换成为json字符串,str
print(json.dumps(a,separators=[',',':']))#去掉空格
d={'b':None,'a':5,'c':'abc'}


print(json.dumps(d,sort_keys=True))#按key排序
print(json.loads('[1,2,"abc",{"age":13,"name":"doudou"}]'))#json->list
