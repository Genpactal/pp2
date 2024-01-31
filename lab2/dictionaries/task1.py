car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#ex1
print(car.get("model"))
#ex2
car["year"]=2020
#ex3
car["color"]="red"
#ex4
car.pop("model")
#ex5
car.clear()