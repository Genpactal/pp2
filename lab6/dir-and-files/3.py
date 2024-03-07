import os 

a = input()

if os.path.exists(a):
    print(os.path.basename(a))
    print(os.path.dirname(a))
else:
    print("bebra")