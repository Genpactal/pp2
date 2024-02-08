import math
def filter_prime(listOfNumbers):
    a=True
    listOfPrimes=[]
    for x in listOfNumbers:
        a=True
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                a=False
        if a==True:
            listOfPrimes.append(x)    
    return listOfPrimes


listOfNumbers=[2,3,4,5,6,7,8,9]
print(filter_prime(listOfNumbers))