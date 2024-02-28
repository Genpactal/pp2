import re

text = str(input())

x = re.sub(r"([A-Z])", lambda bebra: "_" + bebra.group(1).lower(), text)

print(x)