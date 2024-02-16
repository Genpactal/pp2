class MyNums:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.stop:
            raise StopIteration
        x = self.start*self.start
        self.start += 1
        return x
a=int(input())
b=int(input())    
mynums = MyNums(a,b)


# not infinite anymore
for num in mynums:
    print(num, end=' ')