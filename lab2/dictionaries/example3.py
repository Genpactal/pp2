thisdict={"brand": "Ford",
  "model": "Mustang",
  "year": 1964}
for x in thisdict:
  print(x)#keys 
  print(thisdict[x])#values

for x in thisdict.values():
  print(x)
for x in thisdict.keys():
  print(x) 
for x, y in thisdict.items():
  print(x, y) 
  
  
mydict = thisdict.copy()
mydict = dict(thisdict)