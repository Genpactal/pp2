thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 
  
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset) 

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)#Add Any Iterable

print(thisset) 



thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset) 



thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset) 


thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset) 