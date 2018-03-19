class floatRange:
    def __init__(self,start,end,step=0.1):
        self.start=start
        self.end=end
        self.step=step
    def __iter__(self):#正向迭代实现原理
        t=self.start
        while t<=self.end:
            yield t
            t+=self.step
    def __reversed__(self):#反向迭代实现原理
        t=self.end
        while t>=self.start:
            yield t
            t-=self.step
for x in floatRange(1.0,4.0,0.5):
    print(x)
print('-------')
for x in reversed(floatRange(1.0,4.0,0.5)):
    print(x)