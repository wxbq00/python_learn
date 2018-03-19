#2-7 如何实现用户的历史记录功能(最多n条)collections.deque/pickle持久存储
#使用collections deque,设定最大元素个数N,如果超过N,就会把最早进入队列的元素给挤掉
#可以用pickle 对队列对象实现持久化存储，再次运行时候可以重新load
from collections import deque
import pickle
from random import randint
import os
result = randint(1,100)#int

print ("result is ",result)
deque1 = deque([],5)

if os.path.isfile("save.data"):
    deque1 = pickle.load(open("save.data"))


while True:
    k = input("\nplease input your guess number: ")#str
    print(type(k))
    if k.isdigit():
       k = int(k)
    elif k == 'h' or k == 'H':
        print ("your input history is ",list(deque1))

    else:
        continue

    if k != result:
        if k > result:
            print( "your number is greater than result\n"  )
        else:
            print ("your number is less than result\n"   )
        deque1.append(k)

    else:
        print ("It was good result...")
        deque1.append(k)
        break


f = open("save.data",'w')

pickle.dump(deque1, f)