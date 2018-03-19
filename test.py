#tuple1=(1,'asd43',3,4)
#print(tuple1[1:5])
#del tuple1
#print(tuple1)
# seq=('age','sex','name')
# dict=dict.fromkeys(seq,10)
# print(dict)
# d={'age':11,'name':'lucas'}
# print(d.get('age'))
# for k,v in d.items():
#     print(k,v)
# dict = {'Name': 'Zara', 'Age': 7}
# dict2 = {'Sex': 'female' }
# dict.update(dict2)
# print(dict)
import random


def R():
    print(random.randint(1, 1000))


for i in range(1, 10):
    R()