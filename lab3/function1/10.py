
def unique(a):
    b = []
    for i in a:
        if a.count(i) == 1:
            b.append(i)
    
    return b    


a = list(map(int, input().split()))

print(unique(a))
