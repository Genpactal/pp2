import re

file = open("row.txt", "r", encoding="utf8")

text = file.read()

x = re.findall(r"[А-Я][а-я]+", text)               #x = re.findall(r"[A-Z][a-z]+", text) originally

print(x)