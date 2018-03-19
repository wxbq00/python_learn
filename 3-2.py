from collections import Iterable
from collections import Iterator
from random import randint
#如何实现可迭代对象和迭代器对象(2) BookIterable/BookIterator
class BookIterator(Iterator):#迭代器对象
    def __init__(self,books):
        self.books = books
        self.index = 0

    def getBookPrice(self,book):
        return book,randint(1,50),randint(60,100)

    def __next__(self):
        if self.index == len(self.books):#最后一个
            raise StopIteration
        book = self.books[self.index]
        self.index += 1
        return self.getBookPrice(book)

class BookIterable(Iterable):#可迭代对象
    def __init__(self,books):
        self.books = books

    def __iter__(self):
        return BookIterator(self.books)

if __name__ == '__main__':
    for book in sorted(BookIterable(['chinse','math','english'])):
        print (book)