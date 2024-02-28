import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

x = re.sub(r"[ .,]",":", text)

print(x)