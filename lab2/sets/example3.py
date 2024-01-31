thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) 
  

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3) 



set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1) 


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)#elements present in both sets
#symmetric_difference_update() keeps all except dublicates
print(x) 

"""
add()	         Adds an element to the set
clear()	         Removes all the elements from the set
copy()	         Returns a copy of the set
difference()	 Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	     Remove the specified item
intersection()	 Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 Returns whether two sets have a intersection or not
issubset()	     Returns whether another set contains this set or not
issuperset()	 Returns whether this set contains another set or not
pop()	         Removes an element from the set
remove()	     Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	         Return a set containing the union of sets
update()	     Update the set with the union of this set and others
"""

