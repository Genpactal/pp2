def spy_game(x):

    val = ""

    for i in x:
        if x[i]==0 or x[i]==7:
            val = str(val) + str(x[i])
        
    if "007" in val:
        return True
    else:
        return False

list= list(map(int, input().split()))

print(spy_game(list))