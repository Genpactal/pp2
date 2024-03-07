import os

os.chdir('../')
path = os.getcwd()

print("----------")
for x in os.listdir(path):
    path1 = os.path.join(path , x)
    if os.path.isdir(path1):
        print(x)

print("----------")
for y in os.listdir(path):
    path2 = os.path.join(path, y)
    if os.path.isfile(path2):
        print(y)

print("----------")
for item in os.listdir(path):
   print(item)