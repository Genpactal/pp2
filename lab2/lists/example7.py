fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
# or newlist = [x for x in fruits if "a" in x]
#newlist = [x if x != "banana" else "orange" for x in fruits] 
print(newlist) 