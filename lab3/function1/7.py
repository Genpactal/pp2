def has_33(x):
    for i in range(0,len(x)-1):
        if x[i] == 3 and x[i+1] == 3:
            return True
    return False

x = list(map(int, input().split()))

print(has_33(x))