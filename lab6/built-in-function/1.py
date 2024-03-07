x = list(map(int, input().split()))

def res(x):
    n = 1 
    for i in x:
        n = n * i
    return n

s = res(x)
print(s)