import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

x = re.findall("[A-Z][a-z]+", text) 

print(x)