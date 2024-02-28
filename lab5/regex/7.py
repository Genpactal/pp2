import re

text = str(input())

x = re.sub(r"_([a-z])", lambda bebra: bebra.group(1).upper(), text)

print(x)