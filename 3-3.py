
class primeNumbers(object):#生成器函数
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def isPrimeNumbers(self,k):
        if k<2:
            return False
        for i in range(2,k):
            if k%i==0:
                return False#不是素数
        return True
    def __iter__(self):
        for k in range(self.start,self.end+1):#start到end
            if self.isPrimeNumbers(k):
                yield k
for x in primeNumbers(1,100):
    print(x)

# !/usr/bin/python3
print('###############')
import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
