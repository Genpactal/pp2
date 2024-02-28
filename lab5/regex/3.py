import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

x = re.findall(r"[a-z]+_", text)

print(x)