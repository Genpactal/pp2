def histogram(x):
    for i in x:
        print("*" * i)

x = list(map(int, input().split()))

histogram(x)    