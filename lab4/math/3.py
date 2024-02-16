import math 
numOfSides=int(input())
len=int(input())
pi=math.pi
area=(1/2)*(len*numOfSides)*(len/(2*math.tan(pi/numOfSides)))
print(int(area))