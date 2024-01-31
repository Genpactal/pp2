thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict)) 

thisdict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
} #dict()constructor

x = thisdict["model"]
x = thisdict.get("model")
x = thisdict.keys() 
x = thisdict.values() 
x = thisdict.items() 
 
thisdict["color"] = "white"

if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") 