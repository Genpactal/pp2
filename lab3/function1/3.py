def solve(numheads,numlegs):
    rabbits = (numlegs - 2 * numheads) // 2
    chickens=numheads-rabbits
    return "chickens "+str(chickens)+","+"rabbits "+str(rabbits)


numheads=(int(input()))
numlegs=(int(input()))
print(solve(numheads,numlegs))