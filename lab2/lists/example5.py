thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")#removes the first occurance
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)#If you do not specify the index, the pop() method removes the last item.
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]#can also delete list completely
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)