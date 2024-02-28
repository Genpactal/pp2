import re

text = str(input())

x = re.sub(r"([A-Z])", lambda bebra: " " + bebra.group(1), text)

print(x)