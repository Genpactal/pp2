with open("1.py", "r") as file: # "r" is the default mode
    print(file.readline())

with open("1.py", "r") as file:
    print(file.readlines())

with open("1.py", "r") as file:
    print(file.read())