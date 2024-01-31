thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018 #=
thisdict.update({"year": 2018}) 

thisdict.pop("model")
del thisdict["model"]
thisdict.popitem()#last inserted item
thisdict.clear()
