def myRange(start, stop):
    while start > stop:
        yield start
        start -= 1
n=int(input())
print(list(myRange(n,0)))