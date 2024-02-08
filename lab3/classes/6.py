a = int(input().split())

def prime(element):
    dev = 0
    for i in range(1,element):
        if element % i == 0:
            dev += 1
    if(dev == 1):
        return True
    
    
Primes = list(filter(lambda x: prime(x), a))

print(Primes)